from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


class RiverEntity(CoordinatorEntity):
    """Base class for river gauge entities."""

    def __init__(self, coordinator):
        super().__init__(coordinator)
        self.coordinator = coordinator

    @property
    def device_info(self):
        """Return device information for Home Assistant registry."""
        return {
            "identifiers": {(DOMAIN, "river_gauges")},
            "name": "German River Gauges",
            "manufacturer": "Custom Integration",
            "model": "River Gauge Monitor",
        }
