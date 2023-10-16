from typing import List, Dict
from enum import Enum
import datetime
from typing import Tuple


class ContTypeCol(Enum):
    F = 'Коммерческое предложение'
    S = 'Послать письмо'


class DepartmentTypeCol(Enum):
    F = 'Основной офис'
    S = 'Отдел маркетинга'


class TypeContact:

    def __init__(self, name: str, note: str) -> None:
        self._name = name
        self._note = note

    def update(self, dct: Dict[str, str]):
        pass

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name


class CommercialProposalContact(TypeContact):

    def __init__(
            self, name: str,
            note: str = None,
            tpy: str = ContTypeCol.F,  # Вид контакта
            begin_dt=datetime.datetime.now(),  # Дата начала контакта
            end_dt=datetime.datetime.today() + datetime.timedelta(days=14),  # Дата завершения контакта
            descr: str = None,  # Описание контакта для себя
            data_info: str = None  # Формулировка контакта для клиента
    ) -> None:
        super().__init__(name, note)
        self._tpy = tpy
        self._begin_dt = begin_dt
        self._end_dt = end_dt
        self._descr = descr
        self._data_info = data_info

    def update(self, dct: Dict[str, str]):
        self._descr = dct['descr']
        self._data_info = dct['data_info']
        self._note = dct['note']

    def __repr__(self) -> str:
        return f'Тип: {self._tpy}\nname: {self._name}'


class LetterSentContact(TypeContact):

    def __init__(
            self, name: str,
            note: str = None,
            tpy: str = ContTypeCol.S,  # Вид контакта
            begin_dt=datetime.datetime.now(),  # Дата начала контакта
            end_dt=datetime.datetime.today() + datetime.timedelta(days=14),  # Дата завершения контакта
            descr: str = None,  # Описание контакта для себя
            data_info: str = None  # Формулировка контакта для клиента
    ) -> None:
        super().__init__(name, note)
        self._tpy = tpy
        self._begin_dt = begin_dt
        self._end_dt = end_dt
        self._descr = descr
        self._data_info = data_info

    def update(self, dct: Dict[str, str]):
        self._descr = dct['descr']
        self._data_info = dct['data_info']
        self._note = dct['note']

    def __repr__(self) -> str:
        return f'Тип: {self._tpy}\nname: {self._name}'


class TypeDepartment:

    def __init__(
            self, name: str,  # Наименование подразделения
            is_main,  # это основной офис?
            conts: List[TypeContact] = None  # Контакты подразделения
    ) -> None:
        self._name = name
        self._is_main = is_main
        self._conts = conts if conts else list()

    def set_name(self, name):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def add_contact(self, cont):
        self._conts.append(cont)

    def update_contact(self, old_cont, new_cont):
        self._conts[self._conts.index(old_cont)] = new_cont
        return new_cont

    def exist_contact(self, cont):
        return cont in self._conts

    def is_your_type(self):
        pass

    def __repr__(self) -> str:
        return f'Офис главный? {"да" if self._is_main else "нет"}, имя: {self._name}'


class MainOffice(TypeDepartment):

    def __init__(
            self, name: str,
            is_main=True,
            boss_name: str = None,  # Имя руководителя подразделения
            ofb_boss_name: str = None,  # Официальное обращение к руководителю
            tel=None,  # номер телефона подразделения
            email=None,  # Почтовый адрес подразделения
            tpy=DepartmentTypeCol.F  # Тип подразделения
    ) -> None:
        super().__init__(name, is_main)
        self._boss_name = boss_name
        self._ofb_boss_name = ofb_boss_name
        self._tel = tel
        self._email = email
        self.tpy = tpy

    def is_your_type(self):
        return self.tpy

    def __repr__(self) -> str:
        return f'{{Тип: {self.tpy}, Офис главный? {"да" if self._is_main else "нет"}, имя: {self._name} }}'


class MarketingDepartment(TypeDepartment):

    def __init__(self, name: str,
                 is_main=False,
                 tpy=DepartmentTypeCol.S  # Тип подразделения
                 ) -> None:
        super().__init__(name, is_main)
        self.tpy = tpy

    def is_your_type(self):
        return self.tpy

    def __repr__(self) -> str:
        return f'{{Тип: {self.tpy}, Офис главный? {"да" if self._is_main else "нет"}, имя: {self._name} }}'


class Firm:
    def __init__(
            self, name: str,  # Полное наименование фирмы
            sh_name: str = None,  # Краткое наименование фирмы
            country: str = None,  # Страна
            region: str = None,  # Регион (область)
            town: str = None,  # Город
            street: str = None,  # Улица
            postInx: str = None,  # Почтовый индекс
            date_in: str = None,  # Дата ввода фирмы (начало взаимоотношений)
            email: str = None,  # Почтовый адрес фирмы
            web: str = None,  # URL-адрес сайта
            departments: List[TypeDepartment] = None  # Подразделения фирмы
    ) -> None:
        self.__name = name
        self.__sh_name = sh_name
        self.__country = country
        self.__region = region
        self.__town = town
        self.__street = street
        self.__postInx = postInx
        self.__date_in = date_in
        self.__email = email
        self.__web = web
        self.__departments = departments if departments else list()
        # 5 дополнительных  полей
        self.__additional_fields = {}

    # ------------ геттеры --------------
    def get_name(self):
        return self.__name

    def get_sh_name(self):
        return self.__sh_name

    def get_country(self):
        return self.__country

    def get_region(self):
        return self.__region

    def get_town(self):
        return self.__town

    def get_street(self):
        return self.__street

    def get_postInx(self):
        return self.__postInx

    def get_date_in(self):
        return self.__date_in

    def get_email(self):
        return self.__email

    def get_web(self):
        return self.__web

    def get_all_department(self):
        return self.__departments

    def get_all_additional_field(self):
        return self.__additional_fields

    def get_additional_field(self, key):
        return self.__additional_fields[key]

    def update_additional_field(self, key, value):
        self.__additional_fields[key] = value

    def delete_additional_field(self, key, value):
        del self.__additional_fields[key]

    # ------------------------------------
    def add_cont(self, cont):
        self.get_main().add_contact(cont)
        return True

    def update_cont(self, old, new):
        self.get_main().update_contact(old, new)

    def add_cont_to_department(self, department: TypeDepartment, cont: TypeContact):
        department.add_contact(cont)
        return True

    def exist_contact(self, cont):
        for i in self.__departments:
            if i.exist_contact(cont):
                return True
        return False

    def get_main(self) -> TypeDepartment:
        res = list(filter(lambda x: x._is_main, self.__departments))
        return res[0] if res else None

    def is_main(self, department):
        return self.get_main() == department

    def add_department(self, department: TypeDepartment):
        self.__departments.append(department)

    def add_all_department(self, departments):
        self.__departments += departments
        return self.__departments

    def __repr__(self) -> str:
        return self.__name


class FirmFactory:
    @staticmethod
    def create(name: str):
        return Firm(name=name)

    @staticmethod
    def create_contact(name: str, tpy: ContTypeCol):
        dct = {
            ContTypeCol.F: CommercialProposalContact,
            ContTypeCol.S: LetterSentContact,
        }

        return dct[tpy](name)

    @staticmethod
    def create_department(name: str, tpy: DepartmentTypeCol):
        dct = {
            DepartmentTypeCol.F: MainOffice,
            DepartmentTypeCol.S: MarketingDepartment,
        }

        return dct[tpy](name)


class ListFirm:

    def __init__(self, firms: List[Firm] = None) -> None:
        self.__firms = firms

    def add(self, firm):
        self.__firms.append(firm)

    def all(self):
        return self.__firms

    def find_by_name(self, name) -> List[Firm]:
        return list(filter(lambda i: i.get_name() == name, self.__firms))

    def find_by_country(self, country) -> List[Firm]:
        return list(filter(lambda i: i.get_country() == country, self.__firms))

    def remove(self, firm):
        self.__firms.remove(firm)

    def clear(self):
        self.__firms.clear()
