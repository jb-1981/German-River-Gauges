import logging

_LOGGER = logging.getLogger(__name__)


class PegelOnlineAPI:
    """Simple API client placeholder for river gauge data."""

    def __init__(self):
        self.base_url = "https://example.invalid"

    async def fetch_all(self):
        """Fetch all river data (placeholder)."""
        _LOGGER.debug("Fetching river data from API")

        # Placeholder data for now
        return {
            "rhein": {
                "water_level": 0,
                "flow": 0,
                "temperature": None,
                "trend": "stable",
                "warning": 0,
            },
            "mosel": {
                "water_level": 0,
                "flow": 0,
                "temperature": None,
                "trend": "stable",
                "warning": 0,
            },
            "main": {
                "water_level": 0,
                "flow": 0,
                "temperature": None,
                "trend": "stable",
                "warning": 0,
            },
            "donau": {
                "water_level": 0,
                "flow": 0,
                "temperature": None,
                "trend": "stable",
                "warning": 0,
            },
        }
