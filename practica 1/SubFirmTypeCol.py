from enum import Enum
from SbFirmType import SbFirmType


class SubFirmTypeCol(Enum):
    MAIN_OFFICE = SbFirmType('Главный офис', True)
    MARKETING_DEPARTMENT = SbFirmType('Отдел маркетинга', False)
    SUPPLY_DEPARTMENT = SbFirmType('Отдел снабжения', False)

# создание
# ob1 = SubFirmTypeCol.MAIN_OFFICE.value.clone()
