"""IQOS integration sensor platform."""

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import PERCENTAGE
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import IQOSBLECoordinator
from .api import IQOSBLE
from .const import DOMAIN
from .models import IQOSBLEData

SENSOR_DESCRIPTIONS = [
    SensorEntityDescription(
        key="case_battery",
        translation_key="case_battery",
        device_class=SensorDeviceClass.BATTERY,
        entity_registry_enabled_default=True,
        entity_registry_visible_default=True,
        native_unit_of_measurement=PERCENTAGE,
        state_class=SensorStateClass.MEASUREMENT,
    )
]


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the platform for IQOS."""
    data: IQOSBLEData = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        IQOSBLESensor(
            data.coordinator,
            data.device,
            entry.title,
            description,
        )
        for description in SENSOR_DESCRIPTIONS
    )


class IQOSBLESensor(CoordinatorEntity[IQOSBLECoordinator], SensorEntity):
    """Generic sensor for IQOS."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: IQOSBLECoordinator,
        device: IQOSBLE,
        name: str,
        description: SensorEntityDescription,
    ) -> None:
        """Initialize the sensor."""
        super().__init__(coordinator)
        self._coordinator = coordinator
        self._device = device
        self._key = description.key
        self.entity_description = description
        self._attr_unique_id = f"{device.address}_{self._key}"
        self._attr_device_info = DeviceInfo(
            name=name,
            connections={(dr.CONNECTION_BLUETOOTH, device.address)},
        )
        self._attr_native_value = getattr(self._device, self._key)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_native_value = getattr(self._device, self._key)
        self.async_write_ha_state()

    @property
    def available(self) -> bool:
        """Unavailable if coordinator isn't connected."""
        return self._coordinator.connected and super().available
