from typing import List, Optional

from src.model.characteristic import Characteristic
from src.model.service import Service


def find_telia_finance_switch(services: List[Service], action):
    for s in services:
        if s.flexibleSwitch is not None and s.flexibleSwitch.isTeliaFinance and s.action == action:
            return s
    return None


def find_extra_insurance(services, action, insurance_class):
    for s1 in services:
        if s1.insuranceClass == insurance_class and s1.action == action:
            return s1
    return None


def get_characteristic_value(characteristic: Characteristic) -> Optional[str]:
    ret = characteristic.shortValue

    if not ret or ret.strip() == "":
        ret = characteristic.value

    return ret if ret and ret.strip() != "" else None


def find_characteristic_value(service, characteristic_name: str) -> Optional[str]:
    for characteristic in service.characteristics:
        if characteristic.name == characteristic_name:
            return get_characteristic_value(characteristic)
    return None