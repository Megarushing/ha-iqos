"""IQOS integration binary sensor platform."""

from homeassistant.components.binary_sensor import (
    BinarySensorDeviceClass,
    BinarySensorEntity,
    BinarySensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from . import IQOSBLE, IQOSBLECoordinator
from .const import DOMAIN
from .models import IQOSBLEData

ENTITY_DESCRIPTIONS = (
    BinarySensorEntityDescription(
        key="is_open",
        translation_key="is_open",
        entity_registry_enabled_default=True,
        entity_registry_visible_default=True,
        device_class=BinarySensorDeviceClass.OPENING,
    ),
    BinarySensorEntityDescription(
        key="pen_discharged",
        translation_key="pen_discharged",
        entity_registry_enabled_default=True,
        entity_registry_visible_default=True,
        device_class=BinarySensorDeviceClass.BATTERY,
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up the platform for IQOS."""
    data: IQOSBLEData = hass.data[DOMAIN][entry.entry_id]
    async_add_entities(
        IQOSBLEBinarySensor(data.coordinator, data.device, entry.title, description)
        for description in ENTITY_DESCRIPTIONS
    )


class IQOSBLEBinarySensor(CoordinatorEntity[IQOSBLECoordinator], BinarySensorEntity):
    """Pen Battery sensor for IQOS."""

    _attr_has_entity_name = True

    def __init__(
        self,
        coordinator: IQOSBLECoordinator,
        device: IQOSBLE,
        name: str,
        description: BinarySensorEntityDescription,
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
        self._attr_is_on = getattr(self._device, self._key)

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        self._attr_is_on = getattr(self._device, self._key)
        self.async_write_ha_state()

    @property
    def available(self) -> bool:
        """Unavailable if coordinator isn't connected."""
        return self._coordinator.connected and super().available
