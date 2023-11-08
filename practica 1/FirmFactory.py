from typing import Dict

from Firm import Firm
from SbFirmType import SbFirmType
from SubFirm import SubFirm


class FirmFactory:

    def __init__(self, usr_fields=None) -> None:
        self.usr_fields: Dict[str] = usr_fields

    def create(self, name: str=None, region: str=None) -> Firm:
        return Firm(name, region, self.usr_fields)
