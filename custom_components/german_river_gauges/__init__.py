from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .api import PegelOnlineAPI
from .coordinator import RiverDataCoordinator


async def async_setup(hass: HomeAssistant, config: dict):
    """YAML setup not used."""
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up integration from config entry."""

    api = PegelOnlineAPI()
    coordinator = RiverDataCoordinator(hass, api)

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload integration."""
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
