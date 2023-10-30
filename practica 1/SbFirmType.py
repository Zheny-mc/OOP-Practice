class SbFirmType:
    def __init__(self, name, is_main):
        self.__name: str = name
        self.__is_main: bool = is_main

    @property
    def is_main(self):
        return self.__is_main

    @is_main.setter
    def is_main(self, value):
        self.__is_main = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def clone(self):
        return self.__class__(self.name, self.is_main)

    def __repr__(self) -> str:
        return f'SbFirmType{{name={self.__name}, is_main={self.__is_main}}}'

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, SbFirmType):
            raise TypeError("Операнд справа должен иметь тип Contact")

        return self.__name == __o.__name and self.is_main == __o.__is_main

