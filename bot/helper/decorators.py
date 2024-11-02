import asyncio
import random
from collections.abc import Callable
from functools import wraps

from pydantic import BaseModel

from bot.config.settings import config
from bot.core.models import GQLBotApi


def error_handler(delay=5):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            try:
                return await func(*args, **kwargs)
            except Exception:
                await asyncio.sleep(random.randint(delay, delay * 2))
                raise

        return wrapper

    return decorator


def handle_request(
    gql_schema: BaseModel,
    endpoint: str = "/graphql",
    full_url: bool = False,
    method: str = "POST",
    raise_for_status: bool = True,
    json_body: dict | None = None,
):
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        async def wrapper(self, *args, **kwargs):
            url = endpoint if full_url else config.base_url + endpoint
            if method.upper() == "POST":
                _json_body = kwargs.get("json_body") or json_body or {}
                response = await self.http_client.post(url, json=GQLBotApi.get_body(gql_schema, _json_body))
            elif method.upper() == "GET":
                response = await self.http_client.get(url)
            else:
                msg = "Unsupported HTTP method"
                raise ValueError(msg)
            if raise_for_status:
                response.raise_for_status()

            content_type = response.headers.get("Content-Type", "")
            if "application/json" in content_type:
                response_data = await response.json()
            elif "text/" in content_type:
                response_data = await response.text()
            else:
                response_data = await response.read()
            await asyncio.sleep(random.uniform(0.5, 2.1))
            return await func(self, response_json=response_data, **kwargs)

        return wrapper

    return decorator
