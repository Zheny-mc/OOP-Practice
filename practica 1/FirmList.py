from typing import List

from Firm import Firm


class FirmList:
    def __init__(self, firms) -> None:
        self.__firms: List[Firm] = firms

    def find(self, parameter: str, value: str) -> List[Firm]:
        result = list(filter(lambda o: getattr(o, parameter) == value, self.__firms))
        return result if len(result) > 0 else self.__firms

    def add(self, firm: Firm):
        self.__firms.append(firm)

    def remove(self, firm):
        self.__firms.remove(firm)

    def clear(self):
        self.__firms.clear()
