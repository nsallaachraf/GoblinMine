from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

logo = """

"""


class BaseBotSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True, extra="allow")

    API_ID: int
    API_HASH: str

    NIGHT_MOD: bool = True
    NIGHT_TIME: list[int] = [23, 6]

    SLEEP_BETWEEN_START: list[int] = [10, 20]
    SESSION_AC_DELAY: int = 10

    ERRORS_BEFORE_STOP: int = 5

    USE_PROXY_FROM_FILE: bool = False
    ADD_LOCAL_MACHINE_AS_IP: bool = False

    RANDOM_SLEEP_TIME: int = 8

    BOT_SLEEP_TIME: list[int] = [3000, 3500]

    LOGIN_CACHE_TTL: int = 3600
    REF_ID: str = "6218943204"
    auth_header: str = "Authorization"
    base_url: str = "https://api.goblinmine.game"
    bot_name: str = "GoblinMine_bot"
    bot_app: str = "start"


class Settings(BaseBotSettings):
    AUTO_UPGRADE_MINE_LEVEL: bool = True
    AUTO_UPGRADE_MINE: bool = True
    ROTATE_SPIN: bool = True
    UPGRADE_INVENTORY: bool = True
    AUTO_UPGRADE_MINERS: bool = True
    AUTO_UPGRADE_CART: bool = True
    MAX_CART_LEVEL: int = 3
    MAX_CART_PRICE: int = 200_000
    SEND_EXPEDITION: bool = True
    EXPEDITION_COSTS: int = Field(default=20_000, ge=10_000)


config = Settings()
