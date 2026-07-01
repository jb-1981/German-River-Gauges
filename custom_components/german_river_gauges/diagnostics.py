async def async_get_config_entry_diagnostics(hass, entry):
    """Return diagnostics data for Home Assistant."""
    return {
        "entry": entry.data,
        "status": "ok",
    }
