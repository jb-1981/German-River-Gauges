import aiohttp
import logging

_LOGGER = logging.getLogger(__name__)


class PegelOnlineAPI:
    """Client for PEGELONLINE river gauge API."""

    def __init__(self):
        self.base_url = "https://www.pegelonline.wsv.de/webservices/rest-api/v2"

    async def fetch_station_data(self, session: aiohttp.ClientSession, station_id: str):
        """Fetch data for a single station."""
        url = f"{self.base_url}/stations/{station_id}/W/measurements.json"

        async with session.get(url, timeout=10) as resp:
            if resp.status != 200:
                _LOGGER.warning("API error %s for station %s", resp.status, station_id)
                return None

            return await resp.json()

    async def fetch_all(self):
        """Placeholder aggregator (will be expanded next step)."""

        # First real test: one station (Köln/Rhein example)
        station_id = "27300720"  # Rhein Köln

        import aiohttp

        async with aiohttp.ClientSession() as session:
            data = await self.fetch_station_data(session, station_id)

        if not data:
            return {}

        try:
            latest = data[-1]["value"] if isinstance(data, list) else None
        except Exception:
            latest = None

        return {
            "rhein": {
                "water_level": latest,
                "flow": None,
                "temperature": None,
                "trend": "unknown",
                "warning": 0,
            }
        }
