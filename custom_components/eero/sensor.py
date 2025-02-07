"""Sensor platform for the Eero integration."""
from homeassistant.helpers.entity import Entity
from .const import DOMAIN

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up sensor entities for Eero."""
    coordinator = hass.data[DOMAIN][config_entry.entry_id]["coordinator"]
    async_add_entities([EeroStatusSensor(coordinator)], True)

class EeroStatusSensor(Entity):
    """Representation of an Eero status sensor."""

    def __init__(self, coordinator):
        """Initialize the sensor."""
        self.coordinator = coordinator
        self._attr_name = "Eero Status"
        self._state = None

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update sensor state from coordinator data."""
        await self.coordinator.async_request_refresh()
        data = self.coordinator.data or {}
        status = data.get("status", "unknown")
        devices = data.get("devices", [])
        self._state = f"{status} ({len(devices)} devices)"
