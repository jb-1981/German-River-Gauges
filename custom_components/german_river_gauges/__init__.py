import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .api import PegelOnlineAPI
from .coordinator import RiverDataCoordinator

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["sensor"]


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up integration."""

    api = PegelOnlineAPI()
    coordinator = RiverDataCoordinator(hass, api)

    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = coordinator

    # Sensor Plattform laden
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    _LOGGER.warning("German River Gauges loaded")

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data[DOMAIN].pop(entry.entry_id, None)
    return True
