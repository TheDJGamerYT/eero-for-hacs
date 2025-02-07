"""Config flow for the Eero integration."""
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN

LOGIN_METHODS = {
    "eero": "Eero Account",
    "amazon": "Amazon Account"
}

class EeroConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Eero."""
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is None:
            return self.async_show_form(
                step_id="user",
                data_schema=vol.Schema({
                    vol.Required("login_method", default="eero"): vol.In(LOGIN_METHODS),
                    vol.Required("username"): str,
                    vol.Required("password"): str,
                }),
                errors={},
            )

        return self.async_create_entry(title="Eero", data=user_input)
