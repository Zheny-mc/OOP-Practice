from typing import List

from Firm import Firm


class FirmFactory:
    usr_fields: List[str] = list()

    @classmethod
    def create(cls, name=None, region=None, flds=None) -> Firm:
        return Firm(name=name, region=region, usr_fields=flds)