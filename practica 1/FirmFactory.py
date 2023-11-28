from typing import Dict, List

from Firm import Firm


class FirmFactory:
    name: str = ''
    region: str = ''
    usr_fields: Dict[str, str] = {
        "field1": "",
        "field2": "",
        "field3": "",
        "field4": "",
        "field5": ""
    }

    @classmethod
    def create(cls) -> Firm:
        return Firm(cls.name, cls.region, cls.usr_fields)
