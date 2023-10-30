
class ContType:
    def __init__(self, name=None, note=None):
        self.__name: str = name
        self.__note: str = note

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def note(self):
        return self.__note

    @note.setter
    def note(self, value):
        self.__note = value

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, ContType):
            raise TypeError("Операнд справа должен иметь тип ContType")

        return (self.__name == __o.__name and
                self.__note == __o.__note)

    def __hash__(self) -> int:
        return hash((self.__name, self.__note))


