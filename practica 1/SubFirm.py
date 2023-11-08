from typing import List

from Contact import Contact
from SbFirmType import SbFirmType


class SubFirm:

    def __init__(self, sb_firmtpy=None) -> None:
        self.__boss_name: str = None
        self.__email: str = None
        self.__name: str = None
        self.__ofc_boss_name: str = None
        self.__tel: str = None

        self.contacts: List[Contact] = list()
        self.sb_firmtpy: SbFirmType = sb_firmtpy

    # ---------- геттеры и сеттеры -----------
    @property
    def boss_name(self):
        return self.__boss_name

    @boss_name.setter
    def boss_name(self, value):
        self.__boss_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def ofc_boss_name(self):
        return self.__ofc_boss_name

    @ofc_boss_name.setter
    def ofc_boss_name(self, value):
        self.__ofc_boss_name = value

    @property
    def tel(self):
        return self.__tel

    @tel.setter
    def tel(self, value):
        self.__tel = value

    # ------------ методы ---------------
    def add_contact(self, new_contact):
        self.contacts.append(new_contact)

    def exist_contact(self, contact_for_search: Contact) -> bool:
        for cur_contact in self.contacts:
            if cur_contact == contact_for_search:
                return True
        return False

    def is_your_type(self, _type: SbFirmType) -> bool:
        return SbFirmType.is_main == _type.is_main

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, SubFirm):
            raise TypeError("Операнд справа должен иметь тип SubFirm")

        return (self.__boss_name == __o.boss_name and
                self.__email == __o.__email and
                self.__name == __o.__name and
                self.__ofc_boss_name == __o.__ofc_boss_name and
                self.__tel == __o.__tel and
                self.contacts == __o.contacts and
                self.sb_firmtpy == __o.sb_firmtpy)

    def __hash__(self) -> int:
        return hash((self.__boss_name,
                     self.__email,
                     self.__name,
                     self.__ofc_boss_name,
                     self.__tel,
                     self.contacts,
                     self.sb_firmtpy))



