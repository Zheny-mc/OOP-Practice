import unittest

from SbFirmType import SbFirmType
from models import *


class TestFirm(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.usr_field = {
             "filed_name1": "val1",
             "filed_name2": "val2",
             "filed_name3": "val3",
             "filed_name4": "val4",
             "filed_name5": "val5"
        }
        self.firmFactory = FirmFactory(self.usr_field)

    def test_create_firm_factory(self):
        """ проверка правильности создания фирмы фабрикой """
        firm1: Firm = self.firmFactory.create('firm1')
        firm2: Firm = Firm('firm1', usr_fields=self.usr_field)
        # проверка, что существуют пользовательские поля
        if firm1.usr_fields == firm2.usr_fields:
            # проверка, что существует основное подразделение
            if firm1.get_main() == firm2.get_main():
                self.assertEqual(firm1, firm2)
            else:
                raise ValueError("Отсутсвует главное подразедение в 'firm1'")
        else:
            raise ValueError("Отсутсвуют пользовательские поля в фирме 'firm1'")

    def test_find_nizhny_novgorod_firms(self):
        """ правильность создания нижегородских фирм """
        firm1: Firm = self.firmFactory.create('firm', 'Нижний Новгород')
        firm2: Firm = self.firmFactory.create('firm', 'Нижний Новгород')
        firm3: Firm = self.firmFactory.create('firm', 'Москва')

        list_firms: FirmList = FirmList([firm1, firm2, firm3])
        result = list_firms.find('region', 'Нижний Новгород')
        self.assertEqual(len(result), 2)

    def test_add_to_sb_firm(self):
        '''добавление подразделения'''
        test: Firm = self.firmFactory.create()
        new_sub: SubFirm = SubFirm()
        old_count: int = len(test.sb_firms)
        test.add_sb_firm(new_sub)
        new_count: int = len(test.sb_firms)
        self.assertEqual(old_count + 1, new_count)

    def test_addField(self):
        """ добавление поля """
        test: Firm = self.firmFactory.create()
        key, value = "field_name", "val"
        test.add_field(key, value)
        search_value: str = test.get_field(key)
        self.assertEqual(value, search_value)

    def test_get_field(self):
        """ получение поля """
        test: Firm = self.firmFactory.create()
        key, value = "filed_name1", "val1"
        search_value = test.get_field(key)
        self.assertEqual(value, search_value)

    def test_rename_field(self):
        """переименовывание поля"""
        test: Firm = self.firmFactory.create()
        old_key = "field_name_1"
        new_key = "field_name_2"
        value = "value"
        test.add_field(old_key, value)
        test.rename_field(old_key, new_key)
        search_value = test.get_field(new_key)
        self.assertEqual(value, search_value)

    def test_add_cont_to_sub_firm(self):
        """ добавление контакта к подразделениям """
        test_firm: Firm = self.firmFactory.create()
        sub_firm: SubFirm = SubFirm()
        sub_firm_2: SubFirm = SubFirm()

        test_cont: Contact = Contact(ContType())
        test_firm.add_sb_firm(sub_firm)
        test_firm.add_sb_firm(sub_firm_2)
        test_firm.add_cont_to_sb_firm(test_cont)
        self.assertEqual(sub_firm.contacts[-1], sub_firm_2.contacts[-1])

    def test_set_field(self):
        """ установка поля """
        test: Firm = self.firmFactory.create()
        key = "field_name"
        old_value = "val_1"
        new_value = "val_2"

        test.add_field(key, old_value)
        test.set_field(key, new_value)
        search_value = test.get_field(key)
        self.assertEqual(new_value, search_value)


if __name__ == '__main__':
    unittest.main()
