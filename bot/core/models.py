from datetime import datetime
from typing import NamedTuple

from pydantic import BaseModel, Field


class SessionData(BaseModel):
    user_agent: str = Field(validation_alias="User-Agent")
    proxy: str | None = None


class Shema(BaseModel):
    operationName: str
    query: str


class GQLBotApi(NamedTuple):
    login = Shema(
        operationName="login",
        query="mutation login($input: LoginInput!) {\n  login(input: $input) {\n    status\n    token\n    user {\n      id\n      first_name\n      language_code\n      last_name\n      username\n      __typename\n    }\n    __typename\n  }\n}",
    )
    mines_and_task = Shema(
        operationName="minesAndCheckTasksCompleted",
        query="query minesAndCheckTasksCompleted($worldId: Int!) {\n  mines(worldId: $worldId) {\n    ...MINE_FRAGMENT\n    __typename\n  }\n  check_tasks_completed(worldId: $worldId)\n}\n\nfragment MINE_FRAGMENT on MineFool {\n  deposit_day\n  goblin_image\n  id\n  image\n  income_per_day\n  level\n  miner_amount\n  name\n  price\n  user_miners_count\n  volume\n  userMine {\n    auto\n    cart_level\n    deposit_day\n    deposit_day_default\n    extracted_amount\n    extracted_percent\n    id\n    income_hour\n    next_volume\n    updateIn\n    volume\n    updated_at\n    total_day\n    __typename\n  }\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  miningCurrency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}",
    )
    worlds = Shema(
        operationName="worlds",
        query="query worlds {\n  worlds {\n    active\n    icon\n    income_day\n    name\n    id\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}",
    )

    pickUp = Shema(
        operationName="pickUp",
        query="mutation pickUp($input: PickUpMineInput!) {\n  pickUp(input: $input) {\n    total\n    __typename\n  }\n}",
    )

    spinHistoryAndSpins = Shema(
        operationName="spinHistoryAndSpins",
        query="query spinHistoryAndSpins($first: Int!, $page: Int!) {\n  spinHistory(first: $first, page: $page) {\n    ...SPIN_HISTORY_FRAGMENT\n    __typename\n  }\n  spins {\n    ...SPINS_FRAGMENT\n    __typename\n  }\n}\n\nfragment SPIN_HISTORY_FRAGMENT on SpinsHistoryPaginator {\n  data {\n    amount\n    created_at\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n  paginatorInfo {\n    currentPage\n    lastPage\n    perPage\n    total\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}\n\nfragment SPINS_FRAGMENT on SpinsGame {\n  available\n  spins {\n    amount\n    id\n    title\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n  __typename\n}",
    )

    rotateSpin = Shema(
        operationName="rotateSpin",
        query="mutation rotateSpin {\n  rotateSpin {\n    message\n    status\n    sector_won\n    __typename\n  }\n}",
    )

    buyMine = Shema(
        operationName="buyMine",
        query="mutation buyMine($input: BuyMineInput!) {\n  buyMine(input: $input) {\n    message\n    status\n    __typename\n  }\n}",
    )

    mineAndMiners = Shema(
        operationName="mineAndMiners",
        query="query mineAndMiners($mineId: Int!) {\n  mine(mineId: $mineId) {\n    ...MINE_FRAGMENT\n    __typename\n  }\n  miners(mineId: $mineId) {\n    ...MINERS_FRAGMENT\n    __typename\n  }\n}\n\nfragment MINE_FRAGMENT on MineFool {\n  deposit_day\n  goblin_image\n  id\n  image\n  income_per_day\n  level\n  miner_amount\n  name\n  price\n  user_miners_count\n  volume\n  userMine {\n    auto\n    cart_level\n    deposit_day\n    deposit_day_default\n    extracted_amount\n    extracted_percent\n    id\n    income_hour\n    next_volume\n    updateIn\n    volume\n    updated_at\n    total_day\n    __typename\n  }\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  miningCurrency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}\n\nfragment MINERS_FRAGMENT on Miners {\n  available\n  id\n  level\n  name\n  price\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  minerLevel {\n    available\n    disabled\n    existInventoryLevel\n    id\n    image\n    income_hour\n    level\n    name\n    price\n    inventoryLevel {\n      level\n      name\n      __typename\n    }\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n  __typename\n}",
    )
    buyMiner = Shema(
        operationName="buyMiner",
        query="mutation buyMiner($input: BuyMinerInput!) {\n  buyMiner(input: $input) {\n    message\n    status\n    __typename\n  }\n}",
    )

    mineAndUpgradeMine = Shema(
        operationName="mineAndUpgradeMine",
        query="query mineAndUpgradeMine($mineId: Int!) {\n  mine(mineId: $mineId) {\n    ...MINE_FRAGMENT\n    __typename\n  }\n  upgradeMine(mineId: $mineId) {\n    ...UPGRADE_MINE_FRAGMENT\n    __typename\n  }\n}\n\nfragment MINE_FRAGMENT on MineFool {\n  deposit_day\n  goblin_image\n  id\n  image\n  income_per_day\n  level\n  miner_amount\n  name\n  price\n  user_miners_count\n  volume\n  userMine {\n    auto\n    cart_level\n    deposit_day\n    deposit_day_default\n    extracted_amount\n    extracted_percent\n    id\n    income_hour\n    next_volume\n    updateIn\n    volume\n    updated_at\n    total_day\n    __typename\n  }\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  miningCurrency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}\n\nfragment UPGRADE_MINE_FRAGMENT on upgradeMine {\n  id\n  image\n  level\n  name\n  price\n  disabled\n  deposit_day\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  need_inventory {\n    level\n    name\n    __typename\n  }\n  __typename\n}",
    )

    inventory = Shema(
        operationName="inventory",
        query="query inventory($mineId: Int!) {\n  inventory(mineId: $mineId) {\n    disabled\n    id\n    image\n    income_hour\n    level\n    name\n    price\n    inventory_income_hour\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}",
    )

    carts = Shema(
        operationName="carts",
        query="query carts($mineId: Int!, $userMineId: Int!) {\n  carts(mineId: $mineId, userMineId: $userMineId) {\n    auto\n    available\n    id\n    image\n    level\n    name\n    price\n    volume\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    miningCurrency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}",
    )

    buyInventory = Shema(
        operationName="buyInventory",
        query="mutation buyInventory($id: Int!) {\n  buyInventory(id: $id) {\n    message\n    volume\n    status\n    __typename\n  }\n}",
    )

    buyUpgradeMine = Shema(
        operationName="buyUpgradeMine",
        query="mutation buyUpgradeMine($id: Int!) {\n  buyUpgradeMine(id: $id) {\n    message\n    status\n    volume\n    __typename\n  }\n}",
    )

    buyMinerLevel = Shema(
        operationName="buyMinerLevel",
        query="mutation buyMinerLevel($input: BuyMinerLevelInput!) {\n  buyMinerLevel(input: $input) {\n    balance\n    message\n    status\n    __typename\n  }\n}",
    )

    updateCart = Shema(
        operationName="updateCart",
        query="mutation updateCart($id: Int!) {\n  updateCart(id: $id) {\n    volume\n    status\n    message\n    __typename\n  }\n}",
    )
    ExpeditionsAndUserExpeditions = Shema(
        operationName="ExpeditionsAndUserExpeditions",
        query="query ExpeditionsAndUserExpeditions($worldId: Int!) {\n  expeditions(worldId: $worldId) {\n    ...EXPEDITIONS_FRAGMENT\n    __typename\n  }\n  userExpeditions(worldId: $worldId) {\n    ...USER_EXPEDITIONS_FRAGMENT\n    __typename\n  }\n}\n\nfragment EXPEDITIONS_FRAGMENT on Expedition {\n  duration\n  duration_human\n  id\n  image\n  max\n  min\n  name\n  userExpedition\n  userExpeditionAmount\n  userExpeditionDuration\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  expeditionProfit {\n    amount\n    percent\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}\n\nfragment USER_EXPEDITIONS_FRAGMENT on UserExpeditions {\n  amount\n  created_at\n  status\n  name\n  image\n  id\n  price\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  __typename\n}",
    )

    expedition = Shema(
        operationName="expedition",
        query="query expedition($Id: Int!) {\n  expedition(Id: $Id) {\n    ...EXPEDITIONS_FRAGMENT\n    __typename\n  }\n}\n\nfragment EXPEDITIONS_FRAGMENT on Expedition {\n  duration\n  duration_human\n  id\n  image\n  max\n  min\n  name\n  userExpedition\n  userExpeditionAmount\n  userExpeditionDuration\n  currency {\n    ...CURRENCY_FRAGMENT\n    __typename\n  }\n  expeditionProfit {\n    amount\n    percent\n    currency {\n      ...CURRENCY_FRAGMENT\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment CURRENCY_FRAGMENT on Currency {\n  id\n  amount\n  coefficient\n  icon\n  name\n  __typename\n}",
    )

    buyExpedition = Shema(
        operationName="buyExpedition",
        query="mutation buyExpedition($id: Int!, $amount: Int!) {\n  buyExpedition(id: $id, amount: $amount) {\n    message\n    status\n    __typename\n  }\n}",
    )

    @staticmethod
    def get_body(type: Shema, input: dict) -> dict:
        return type.model_dump() | {"variables": input}


class Currency(BaseModel):
    id: int
    amount: float | None
    coefficient: str
    icon: str
    name: str


class Worlds(BaseModel):
    active: bool
    icon: str
    income_day: float
    name: str
    id: int
    currency: Currency
    __typename: str


class UserMine(BaseModel):
    auto: bool
    cart_level: int
    deposit_day: float
    deposit_day_default: float
    extracted_amount: float
    extracted_percent: float
    id: int
    income_hour: float
    next_volume: str
    updateIn: int
    volume: int
    updated_at: datetime
    total_day: float | None
    __typename: str


class SpinsHistory(BaseModel):
    amount: int
    created_at: datetime
    currency: Currency
    __typename: str


class MineFool(BaseModel):
    deposit_day: int
    goblin_image: str
    id: int
    image: str
    income_per_day: int
    level: int
    miner_amount: int
    name: str
    price: int
    user_miners_count: int | None
    volume: int
    userMine: UserMine | None
    currency: Currency
    miningCurrency: Currency
    __typename: str


class Inventory(BaseModel):
    __typename: str
    currency: dict | None = None
    disabled: bool
    id: int | None = None
    image: str
    income_hour: float | None = None
    inventory_income_hour: float
    level: int | None = None
    name: str
    price: float | None = None


class UpgradeMine(BaseModel):
    id: int
    image: str
    level: int
    name: str
    price: float
    disabled: bool
    deposit_day: int
    currency: Currency
    need_inventory: dict | None = None
    __typename: str


class NeedInventory(BaseModel):
    level: int
    name: str
    __typename: str


class MinerLevel(BaseModel):
    available: bool
    disabled: bool | None = None
    existInventoryLevel: bool
    id: int
    image: str
    income_hour: float
    level: int
    name: str
    price: int
    inventoryLevel: NeedInventory | None = None
    currency: Currency
    __typename: str


class Miners(BaseModel):
    available: bool
    id: int
    level: int
    name: str
    price: int
    currency: Currency
    minerLevel: list[MinerLevel]
    __typename: str


class Cart(BaseModel):
    auto: bool
    available: bool
    id: int
    image: str
    level: int
    name: str
    price: int
    volume: int
    currency: Currency
    miningCurrency: Currency
    __typename: str


class UserExpeditions(BaseModel):
    amount: int | None
    created_at: datetime
    status: str
    name: str
    image: str
    id: int
    price: int
    currency: Currency
    __typename: str
