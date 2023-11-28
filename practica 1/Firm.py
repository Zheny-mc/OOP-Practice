from typing import Dict, List

from Contact import Contact
from SbFirmType import SbFirmType
from SubFirm import SubFirm
from SubFirmTypeCol import SubFirmTypeCol


class Firm:

    def __init__(self, name: str = None,
                 region: str = None,
                 usr_fields: Dict[str, str] = None):
        self.usr_fields: Dict[str, str] = usr_fields if usr_fields else {}
        self.sb_firms: List[SubFirm] = list()
        self.contacts: List[Contact] = list()

        self.__country: str = None
        self.__email: str = None
        self.__date_in: str = None
        self.__name: str = name
        self.__region: str = region
        self.__post_inx: str = None
        self.__street: str = None
        self.__town: str = None
        self.__web: str = None

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def date_in(self):
        return self.__date_in

    @date_in.setter
    def date_in(self, value):
        self.__date_in = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def region(self):
        return self.__region

    @region.setter
    def region(self, value):
        self.__region = value

    @property
    def post_inx(self):
        return self.__post_inx

    @post_inx.setter
    def post_inx(self, value):
        self.__post_inx = value

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, value):
        self.__street = value

    @property
    def town(self):
        return self.__town

    @town.setter
    def town(self, value):
        self.__town = value

    @property
    def web(self):
        return self.__web

    @web.setter
    def web(self, value):
        self.__web = value

    def get_sb_firm_by_tpy(self, tpy: SbFirmType) -> List[SubFirm]:
        return list(filter(lambda x: x.tpy == tpy, self.sb_firms))

    def get_sb_firm(self, index):
        return self.sb_firms[index]

    def set_sb_firm(self, index, value):
        self.sb_firms[index] = value

    def count_sb_firms(self) -> int:
        return len(self.sb_firms)

    # ------------- методы -------------

    def add_cont(self, new_contact: Contact):
        self.contacts.append(new_contact)

    def add_cont_to_sb_firm(self, new_contact: Contact):
        for cur_sub in self.sb_firms:
            cur_sub.add_contact(new_contact.clone())

    def add_field(self, field_name: str, value: str):
        self.usr_fields[field_name] = value

    def add_sb_firm(self, new_sub_firm: SubFirm):
        self.sb_firms.append(new_sub_firm)

    def exist_contact(self, contact_for_search: Contact) -> bool:
        for cur_contact in self.contacts:
            if cur_contact == contact_for_search:
                return True
        return False

    def get_field(self, key: str) -> str:
        if self.usr_fields[key] is not None:
            return self.usr_fields[key]
        else:
            raise ValueError('key not found')

    def rename_field(self, old_key, new_key):
        if old_key in self.usr_fields.keys():
            self.usr_fields[new_key] = self.usr_fields[old_key]
            del self.usr_fields[old_key]
        else:
            raise ValueError('OldKey not found.')

    def set_field(self, field_name: str, value: str):
        self.usr_fields[field_name] = value

    def get_main(self):
        ''' Получить главное подразделение '''
        sb_firm: SubFirm = SubFirmTypeCol.MAIN_OFFICE.value.clone()
        sb_firm.name = self.__name
        sb_firm.email = self.__email
        return sb_firm

    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, Firm):
            raise TypeError("Операнд справа должен иметь тип Firm")

        return (
            self.usr_fields == __o.usr_fields and
            self.sb_firms == __o.sb_firms and
            self.contacts == __o.contacts and
            self.__country == __o.__country and
            self.__date_in == __o.__date_in and
            self.__email == __o.__email and
            self.__name == __o.__name and
            self.__post_inx == __o.__post_inx and
            self.__region == __o.__region and
            self.__street == __o.__street and
            self.__town == __o.__town and
            self.__web == __o.__web
        )

    def __hash__(self) -> int:
        return hash((
            self.usr_fields,
            self.sb_firms,
            self.contacts,
            self.__country,
            self.__date_in,
            self.__email,
            self.__name,
            self.__post_inx,
            self.__region,
            self.__street,
            self.__town,
            self.__web
        ))






