from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN


SENSOR_TYPES = {
    "water_level": ("Wasserstand", "mdi:water"),
    "flow": ("Durchfluss", "mdi:waves"),
    "temperature": ("Temperatur", "mdi:thermometer"),
    "trend": ("Trend", "mdi:trending-up"),
    "warning": ("Warnstufe", "mdi:alert"),
}


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up sensors from a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]

    entities = []

    for river in coordinator.data.keys():
        for sensor_type in SENSOR_TYPES:
            entities.append(
                RiverSensor(coordinator, river, sensor_type)
            )

    async_add_entities(entities)


class RiverSensor(CoordinatorEntity, SensorEntity):
    """Representation of a river gauge sensor."""

    def __init__(self, coordinator, river: str, sensor_type: str):
        """Initialize sensor."""
        super().__init__(coordinator)

        self.coordinator = coordinator
        self.river = river
        self.sensor_type = sensor_type

        name, icon = SENSOR_TYPES[sensor_type]

        self._attr_name = f"{river.capitalize()} {name}"
        self._attr_unique_id = f"{DOMAIN}_{river}_{sensor_type}"
        self._attr_icon = icon

    @property
    def native_value(self):
        """Return sensor value."""
        data = self.coordinator.data or {}
        river_data = data.get(self.river, {})

        return river_data.get(self.sensor_type)

    @property
    def extra_state_attributes(self):
        """Return attributes."""
        return {
            "river": self.river,
            "type": self.sensor_type,
        }

    @property
    def available(self):
        """Return availability."""
        return self.coordinator.data is not None
