from __future__ import annotations

import logging

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

SENSOR_TYPES = {
    "water_level": ("Wasserstand", "mdi:water"),
    "flow": ("Durchfluss", "mdi:waves"),
    "temperature": ("Temperatur", "mdi:thermometer"),
    "trend": ("Trend", "mdi:trending-up"),
    "warning": ("Warnstufe", "mdi:alert"),
}


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry, async_add_entities):
    """Set up sensors."""

    coordinator = hass.data.get(DOMAIN, {}).get(entry.entry_id)

    if not coordinator:
        _LOGGER.error("Coordinator not found")
        return

    entities = []

    data = coordinator.data or {}

    for river in data.keys():
        for sensor_type in SENSOR_TYPES:
            entities.append(
                RiverSensor(coordinator, river, sensor_type)
            )

    async_add_entities(entities)


class RiverSensor(CoordinatorEntity, SensorEntity):
    """River sensor."""

    def __init__(self, coordinator, river: str, sensor_type: str):
        super().__init__(coordinator)

        self.river = river
        self.sensor_type = sensor_type

        name, icon = SENSOR_TYPES[sensor_type]

        self._attr_name = f"{river.capitalize()} {name}"
        self._attr_unique_id = f"{DOMAIN}_{river}_{sensor_type}"
        self._attr_icon = icon

    @property
    def native_value(self):
        data = self.coordinator.data or {}
        river_data = data.get(self.river, {})
        return river_data.get(self.sensor_type)

    @property
    def available(self):
        return self.coordinator.data is not None
