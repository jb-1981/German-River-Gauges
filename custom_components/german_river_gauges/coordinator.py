from datetime import timedelta
import logging

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


class RiverDataCoordinator(DataUpdateCoordinator):
    """Coordinates fetching river data."""

    def __init__(self, hass, api):
        """Initialize coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name="German River Gauges",
            update_interval=timedelta(minutes=15),
        )
        self.api = api

    async def _async_update_data(self):
        """Fetch data from API."""
        return await self.api.fetch_all()
