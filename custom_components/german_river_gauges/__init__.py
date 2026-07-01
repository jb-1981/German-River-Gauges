from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up via YAML is not supported."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up integration from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    return True
