from homeassistant.helpers.entity import Entity

from .const import DOMAIN


SENSOR_TYPES = {
    "water_level": "Water Level",
    "flow": "Flow",
    "temperature": "Temperature",
    "trend": "Trend",
    "warning": "Warning Level",
}


class RiverSensor(Entity):
    """Representation of a river gauge sensor."""

    def __init__(self, coordinator, river, sensor_type):
        self.coordinator = coordinator
        self.river = river
        self.sensor_type = sensor_type

        self._attr_name = f"{river} {SENSOR_TYPES[sensor_type]}"
        self._attr_unique_id = f"{DOMAIN}_{river}_{sensor_type}"

    @property
    def state(self):
        """Return sensor value."""
        data = self.coordinator.data or {}
        river_data = data.get(self.river, {})
        return river_data.get(self.sensor_type)

    @property
    def extra_state_attributes(self):
        """Return additional attributes."""
        return {
            "river": self.river,
            "sensor_type": self.sensor_type,
        }

    @property
    def available(self):
        """Return if sensor is available."""
        return self.coordinator.data is not None
