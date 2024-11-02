import json

from aiocache import Cache, cached
from pydantic import TypeAdapter
from pyrogram import Client

from bot.helper.decorators import error_handler, handle_request

from .base_api import BaseBotApi
from .models import Cart, GQLBotApi, Inventory, MineFool, Miners, UpgradeMine, UserExpeditions, Worlds


class CryptoBotApi(BaseBotApi):
    def __init__(self, tg_client: Client):
        super().__init__(tg_client)

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.login)
    async def login(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.mines_and_task)
    async def mines_and_task(self, *, response_json: dict, json_body: dict) -> list[MineFool]:
        return TypeAdapter(list[MineFool]).validate_python(response_json["data"]["mines"])

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.worlds)
    async def worlds(self, *, response_json: dict) -> list[Worlds]:
        return TypeAdapter(list[Worlds]).validate_python(response_json["data"]["worlds"])

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.pickUp)
    async def claim_mining(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.spinHistoryAndSpins)
    async def spin_history(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.buyMine)
    async def rotate_spin(self, *, response_json: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.buyMine)
    async def buy_mine(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.mineAndMiners)
    async def get_update_miners(self, *, response_json: dict, json_body: dict) -> list[Miners]:
        return TypeAdapter(list[Miners]).validate_python(response_json["data"]["miners"])

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.mineAndUpgradeMine)
    async def get_update_mine(self, *, response_json: dict, json_body: dict) -> list[UpgradeMine]:
        return TypeAdapter(list[UpgradeMine]).validate_python(response_json["data"]["upgradeMine"])

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.inventory)
    async def get_update_inventory(self, *, response_json: dict, json_body: dict) -> list[Inventory]:
        return TypeAdapter(list[Inventory]).validate_python(response_json["data"]["inventory"])

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.carts)
    async def get_update_cart(self, *, response_json: dict, json_body: dict) -> list[Cart]:
        return TypeAdapter(list[Cart]).validate_python(response_json["data"]["carts"])

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.buyInventory)
    async def buy_update_inventory(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.buyUpgradeMine)
    async def buy_upgrade_mine(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.buyMiner)
    async def buy_upgrade_miners(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.buyMinerLevel)
    async def buy_upgrade_miner_level(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.ExpeditionsAndUserExpeditions)
    async def get_expeditions(self, *, response_json: dict, json_body: dict) -> list[UserExpeditions]:
        return TypeAdapter(list[UserExpeditions]).validate_python(response_json["data"]["userExpeditions"])

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.expedition)
    async def send_expedition(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @error_handler()
    @handle_request(gql_schema=GQLBotApi.buyExpedition)
    async def buy_expedition(self, *, response_json: dict, json_body: dict) -> dict:
        return response_json["data"]

    @cached(ttl=2 * 60 * 60, cache=Cache.MEMORY)
    @error_handler()
    @handle_request(
        "https://raw.githubusercontent.com/testingstrategy/musk_daily/main/daily.json",
        method="GET",
        full_url=True,
    )
    async def get_helper(self, *, response_json: str) -> dict:
        return json.loads(response_json)
