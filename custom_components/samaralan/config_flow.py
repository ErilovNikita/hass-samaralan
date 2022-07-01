from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries, exceptions
from homeassistant.core import HomeAssistant
from .const import DOMAIN
from .sst import SST

_LOGGER = logging.getLogger(__name__)

DATA_SCHEMA = vol.Schema({("RouterIP"): str})


async def validate_input(hass: HomeAssistant, data: dict) -> dict[str, Any]:
    if len(data["RouterIP"]) < 3:
        raise InvalidRouterIP

    return {"title": data["RouterIP"]}


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, router_ip = None):

        errors = {}
        if router_ip is not None:
            try:
                info = await validate_input(self.hass, router_ip)
                return self.async_create_entry(title=info["title"], data=router_ip)

            except InvalidRouterIP:
                errors["RouterIP"] = "invalid_router_ip"

        return self.async_show_form(
            step_id="RouterIP", data_schema=DATA_SCHEMA, errors=errors
        )


class InvalidRouterIP(exceptions.HomeAssistantError):
    """Error to indicate we cannot connect."""
