from typing import Dict

from ContType import ContType


class ContTypeCol:
    def __init__(self) -> None:
        self.__dct = Dict[str, ContType]()

    def get(self, index: str) -> ContType:
        return self.__dct[index]

    def update(self, index: str, value: ContType):
        self.__dct[index] = value

    def clear(self):
        self.__dct.clear()
