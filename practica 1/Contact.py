from ContType import ContType


class Contact:
    def __init__(self, tpe: ContType,
                 begin_dt=None,
                 end_dt=None,
                 date_into=None,
                 descr=None) -> None:
        self.__begin_dt: str = begin_dt
        self.__end_dt: str = end_dt
        self.__date_into: str = date_into
        self.__descr: str = descr
        self.__cnt_type: ContType = tpe

    @property
    def begin_dt(self):
        return self.__begin_dt

    @begin_dt.setter
    def begin_dt(self, value):
        self.__begin_dt = value

    @property
    def end_dt(self):
        return self.__end_dt

    @end_dt.setter
    def end_dt(self, value):
        self.__end_dt = value

    @property
    def date_into(self):
        return self.__date_into

    @date_into.setter
    def date_into(self, value):
        self.__date_into = value

    @property
    def descr(self):
        return self.__descr

    @descr.setter
    def descr(self, value):
        self.__descr = value

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Contact):
            raise TypeError("Операнд справа должен иметь тип Contact")

        return (self.__begin_dt == __o.__begin_dt and
                self.__end_dt == __o.__end_dt and
                self.__descr == __o.__descr and
                self.__cnt_type == __o.__cnt_type)

    def __hash__(self) -> int:
        return hash((self.__begin_dt,
                     self.__end_dt,
                     self.__descr,
                     self.__cnt_type))

    # ---------- methods ---------
    def clone(self):
        return self.__class__(
            self.__cnt_type,
            self.__begin_dt,
            self.__end_dt,
            self.__date_into,
            self.__descr
        )
