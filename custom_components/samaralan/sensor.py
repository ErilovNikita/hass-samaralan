from homeassistant.const import (VOLUME_CUBIC_METERS,PERCENTAGE)
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.helpers.entity import Entity

from .const import DOMAIN
from . import sst
import logging
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, config_entry, async_add_entities):
    sst1 = hass.data[DOMAIN][config_entry.entry_id]
    new_devices = []

    #Создать все сенсоры
    for module in sst1.devices:
        for wSensor in module.samaraLan:
            new_devices.append(sensorBalance(wSensor, module))

        if new_devices:
            async_add_entities(module)

class sensorBalance(Entity):
    _attr_unit_of_measurement = 'Р'
    _attr_device_class = SensorDeviceClass.NONE
    _attr_state_class = SensorStateClass.NONE

    def __init__(self, samaraLan, module):
        self._sensor = samaraLan
        self._module = module

        # Уникальный идентификатор
        self._attr_unique_id = f"{DOMAIN}_balance"

        # Отображаемое имя
        self._attr_name = f"Баланс"

        # Текущее значение
        self._state = self._sensor.get_balance

    @property
    def icon(self):
        return "mdi:credit-card-refresh"
