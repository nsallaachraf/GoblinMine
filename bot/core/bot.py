import asyncio
import random
from datetime import datetime

import aiocache
from pyrogram import Client

from bot.config.headers import headers
from bot.config.logger import log
from bot.config.settings import config

from .api import CryptoBotApi
from .models import MineFool, Miners, SessionData, SpinsHistory, Worlds
from .utils import is_current_hour_in_range, num_prettier


class CryptoBot(CryptoBotApi):
    def __init__(self, tg_client: Client, additional_data: dict) -> None:
        super().__init__(tg_client)
        self.authorized = False
        self.sleep_time = config.BOT_SLEEP_TIME
        self.additional_data: SessionData = SessionData.model_validate(
            {k: v for d in additional_data for k, v in d.items()}
        )

    @aiocache.cached(ttl=config.LOGIN_CACHE_TTL)
    async def login_to_app(self, proxy: str | None) -> bool:
        tg_web_data = await self.get_tg_web_data(proxy=proxy)
        res = await self.login(json_body={"input": {"initData": tg_web_data}})
        self.http_client.headers[config.auth_header] = f'Bearer {res["login"]["token"]}'
        return True

    async def perform_auto_upgrade_mine_level(self) -> None:
        for mine in self.miner_data:
            if not mine.userMine and self.total_money > mine.price:
                await self.buy_mine(json_body={"input": {"mineId": mine.id}})
                self.logger.success(f"Auto-upgrade mine <g>{mine.name}</g> cost <r>-{num_prettier(mine.price)}</r>")
                self.total_money -= mine.price

    async def perform_auto_upgrade_mine(self):
        for mine in self.miner_data:
            if mine.userMine:
                self.logger.success(f"🚀 Начало автоматического улучшения шахты <g>{mine.name}</g> 🛠️")

                miners_data = await self.get_update_miners(json_body={"mineId": mine.id})
                if config.UPGRADE_INVENTORY:
                    await self._upgrade_inventory(mine)
                if config.AUTO_UPGRADE_MINE:
                    await self._upgrade_mine(mine)
                if config.AUTO_UPGRADE_MINERS:
                    await self._upgrade_miners(mine, miners_data)
                if config.AUTO_UPGRADE_CART:
                    await self._upgrade_cart(mine)

    async def perform_expeditions(self):
        expedition = await self.get_expeditions(json_body={"worldId": self.world_id})
        for i in expedition:
            if self.total_money > config.EXPEDITION_COSTS:
                if i.status == "in_process":
                    continue
                await self.send_expedition(json_body={"id": i.id})

                await self.buy_expedition({"id": i.id, "amount": config.EXPEDITION_COSTS})
                self.total_money -= config.EXPEDITION_COSTS
                self.logger.info(f"✅ Successfully send expedition <blue>{i.name}</blue> ")

    async def _upgrade_inventory(self, mine: MineFool) -> None:
        self.logger.success(f"🚀 Start of auto-upgrade <g>INVENTORY</g> for mine <g>{mine.name}</g> 🛠️")
        inventory_data = await self.get_update_inventory(json_body={"mineId": mine.id})
        self.inventory_map_data = {i.name: i.level or 100 for i in inventory_data}
        for i in inventory_data:
            if i.disabled or i.price > self.total_money:
                continue
            await self.buy_update_inventory(json_body={"id": i.id})
            self.total_money -= i.price
            self.logger.info(
                f"✅ Successfully upgraded <blue>{i.name}</blue> to level {i.level} 🚀 cost <r>-{num_prettier(i.price)}</r> for mine <g>{mine.name}</g> ✨"
            )
        self.logger.info(f"🏁 Completed auto-upgrade <g>INVENTORY</g> for mine <g>{mine.name}</g> ✨")

    async def _upgrade_mine(self, mine: MineFool) -> None:
        self.logger.success(f"🚀 Start of auto-upgrade <g>MINE</g> for mine <g>{mine.name}</g> 🛠️")
        mine_data = await self.get_update_mine(json_body={"mineId": mine.id})
        for i in mine_data:
            if i.disabled or self.total_money < i.price:
                continue
            await self.buy_upgrade_mine(json_body={"id": i.id})
            self.total_money -= i.price
            self.logger.info(
                f"✅ Successfully upgraded <blue>{i.name}</blue> to level {i.level} 🚀cost <r>-{num_prettier(i.price)}</r>for mine <g>{mine.name}</g> ✨"
            )
        self.logger.info(f"🏁 Completed auto-upgrade <g>MINE</g> for mine <g>{mine.name}</g> ✨")

    async def _upgrade_miners(self, mine: MineFool, miners_data: list[Miners]) -> None:
        self.logger.success(f"🚀 Start of auto-upgrade <g>MINE</g> for mine <g>{mine.name}</g> 🛠️")
        for i in miners_data:
            if not i.available and self.total_money > i.price:
                await self.buy_upgrade_miners(json_body={"input": {"minerId": i.id}})
                self.logger.info(
                    f"🎉 Successfully opened new miner <blue>({i.name})</blue> for mine <g>{mine.name}</g> ⛏️ cost <r>-{num_prettier(i.price)}</r>  for mine <g>{mine.name}</g> ✨"
                )
                self.total_money -= i.price
            for level in i.minerLevel:
                if level.available or level.price > self.total_money:
                    continue
                if (
                    level.inventoryLevel
                    and self.inventory_map_data.get(level.inventoryLevel.name, 100) >= level.inventoryLevel.level
                ):
                    await self.buy_upgrade_miner_level(json_body={"input": {"minerLevelId": level.id}})
                    self.logger.info(
                        f"🚀 Successfully upgraded miner <blue>({i.name})</blue> to new level <blue>({level.name})</blue> for mine <g>{mine.name}</g> 💪cost <r>-{num_prettier(level.price)}</r> for mine <g>{mine.name}</g> ✨"
                    )
                    self.total_money -= i.price
        self.logger.info(f"🏁 Completed auto-upgrade  <g>MINERS</g> for mine <g>{mine.name}</g> ✨")

    async def _upgrade_cart(self, mine: MineFool) -> None:
        cart_data = await self.get_update_cart(json_body={"mineId": mine.id, "userMineId": mine.userMine.id})
        for i in cart_data:
            if i.id > config.MAX_CART_LEVEL or i.price > config.MAX_CART_PRICE:
                break
            if not i.available and self.total_money > i.price:
                await self.buy_upgrade_miners(json_body={"input": {"minerId": i.id}})
                self.logger.info(
                    f"🎉 Successfully upgraded card <blue>({i.name})</blue> for mine <g>{mine.name}</g> ⛏️ cost <r>-{num_prettier(i.price)}</r>  for mine <g>{mine.name}</g> ✨"
                )
                self.total_money -= i.price
                break

    async def execute_tasks(self):
        pass

    async def run(self, proxy: str | None) -> None:
        async with await self.create_http_client(proxy=proxy, headers=headers):
            while True:
                if self.errors >= config.ERRORS_BEFORE_STOP:
                    self.logger.error("Bot stopped (too many errors)")
                    break
                if config.NIGHT_MOD and await is_current_hour_in_range(*config.NIGHT_TIME, self.logger):
                    continue
                try:
                    if await self.login_to_app(proxy):
                        self.my_worlds: list[Worlds] = await self.worlds()
                        self.active_world = world if (world := self.my_worlds[0]) and world.active else None
                        self.total_money = self.active_world.currency.amount
                        self.logger.info(f"Total money <y>{num_prettier(self.active_world.currency.amount)}</y>🪙")
                        self.world_id = self.active_world.id
                    self.miner_data: list[MineFool] = await self.mines_and_task(json_body={"worldId": self.world_id})
                    await self.claim_all_mining()

                    if config.ROTATE_SPIN:
                        res = await self.spin_history(json_body={"first": 15, "page": 1})
                        if history := res["spinHistory"].get("data"):
                            if not history:
                                await self.rotate_spin()
                                self.logger.info("spin {res}")
                            last_spin = SpinsHistory(**history[0])
                            if (datetime.utcnow() - last_spin.created_at).days >= 1:
                                await self.rotate_spin()
                            res = await self.spin_history(json_body={"first": 15, "page": 1})
                            self.logger.info(f"Res {res}")

                    self.miner_data: list[MineFool] = await self.mines_and_task(json_body={"worldId": self.world_id})
                    if config.AUTO_UPGRADE_MINE_LEVEL:
                        await self.perform_auto_upgrade_mine_level()
                    if config.AUTO_UPGRADE_MINE:
                        await self.perform_auto_upgrade_mine()
                    if config.SEND_EXPEDITION:
                        await self.perform_expeditions()
                    sleep_time = random.randint(*config.BOT_SLEEP_TIME)
                    self.logger.info(f"🛌 Sleep time: {sleep_time // 60} minutes 🕒")
                    await asyncio.sleep(sleep_time)

                except RuntimeError as error:
                    raise error from error
                except Exception:
                    self.errors += 1
                    await self.login_to_app.cache.clear()
                    self.logger.exception("Unknown error")
                    await self.sleeper(additional_delay=self.errors * 8)

    async def claim_all_mining(self):
        for miner_data in self.miner_data:
            if miner_data.userMine:
                await self.mines_and_task(json_body={"worldId": self.world_id})
                await self.claim_mining(
                    json_body={"input": {"mineId": miner_data.userMine.id, "worldId": self.world_id}}
                )
                self.total_money += miner_data.userMine.extracted_amount
                self.logger.info(f"Claimed <y>{num_prettier(miner_data.userMine.extracted_amount)}</y>")


async def run_bot(tg_client: Client, proxy: str | None, additional_data: dict) -> None:
    try:
        await CryptoBot(tg_client=tg_client, additional_data=additional_data).run(proxy=proxy)
    except RuntimeError:
        log.bind(session_name=tg_client.name).exception("Session error")
