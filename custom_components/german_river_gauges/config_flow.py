import voluptuous as vol
from homeassistant import config_entries

from .const import DOMAIN, RIVERS, CONF_RIVERS


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for German River Gauges."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """User configuration step."""

        if user_input is not None:
            return self.async_create_entry(
                title="German River Gauges",
                data=user_input,
            )

        schema = vol.Schema(
            {
                vol.Required(CONF_RIVERS, default=list(RIVERS.keys())): vol.In(
                    list(RIVERS.keys())
                )
            }
        )

        return self.async_show_form(
            step_id="user",
            data_schema=schema,
        )
