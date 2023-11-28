import unittest
from typing import Dict

from SbFirmType import SbFirmType
from models import *


class TestFirm(unittest.TestCase):
    @staticmethod
    def getSettingFirmFactory(name, region):
        FirmFactory.name = name
        FirmFactory.region = region
        FirmFactory.usr_fields = {
            "field1": "",
            "field2": "",
            "field3": "",
            "field4": "",
            "field5": ""
        }

        lst_user_field = list(FirmFactory.usr_fields.keys())
        return FirmFactory, lst_user_field

    def test_create_firm_factory(self):
        """ проверка правильности создания фирмы фабрикой """
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        firm1: Firm = firmFactory.create()

        usr_fields: Dict[str, str] = {
            'field1': '',
            'field2': '',
            'field3': '',
            'field4': '',
            'field5': ''
        }
        firm2: Firm = Firm('firm1', 'Нижний Новгород', usr_fields)
        # проверка, что существуют пользовательские поля
        if firm1.usr_fields == firm2.usr_fields:
            # проверка, что существует основное подразделение
            if firm1.get_main() == firm2.get_main():
                self.assertEqual(firm1, firm2)
            else:
                raise ValueError("Отсутсвует главное подразедение в 'firm1'")
        else:
            raise ValueError("Отсутсвуют пользовательские поля в фирме 'firm1'")

    def test_exist_main_sb_firm(self):
        """ Существует главная фирма? """
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        firm: Firm = firmFactory.create()
        self.assertIsNotNone(firm.get_main())

    def test_find_nizhny_novgorod_firms(self):
        """ правильность создания нижегородских фирм """
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        firm1: Firm = firmFactory.create()
        firm2: Firm = firmFactory.create()
        firmFactory.region = 'Москва'
        firm3: Firm = firmFactory.create()

        list_firms: FirmList = FirmList([firm1, firm2, firm3])
        result = list_firms.find('region', 'Нижний Новгород')
        self.assertEqual(len(result), 2)

    def test_add_to_sb_firm(self):
        '''добавление подразделения'''
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        test_firm: Firm = firmFactory.create()
        new_sub: SubFirm = SubFirm()
        old_count: int = len(test_firm.sb_firms)
        test_firm.add_sb_firm(new_sub)
        new_count: int = len(test_firm.sb_firms)
        self.assertEqual(old_count + 1, new_count)

    def test_addField(self):
        """ добавление поля """
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        test: Firm = firmFactory.create()
        key, value = "field6", "val"
        test.add_field(key, value)
        search_value: str = test.get_field(key)
        self.assertEqual(value, search_value)

    def test_get_field(self):
        """ получение поля """
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        test: Firm = firmFactory.create()
        key, value = lst_user_field[1], ''
        search_value = test.get_field(key)
        self.assertEqual(value, search_value)

    def test_rename_field(self):
        """переименовывание поля"""
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        test: Firm = firmFactory.create()
        old_key = "field1"
        new_key = "field1_2"
        value = "value"
        test.add_field(old_key, value)
        test.rename_field(old_key, new_key)
        search_value = test.get_field(new_key)
        self.assertEqual(value, search_value)

    def test_add_cont_to_sub_firm(self):
        """ добавление контакта к подразделениям """
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        test_firm: Firm = firmFactory.create()
        sub_firm: SubFirm = SubFirm()
        sub_firm_2: SubFirm = SubFirm()

        test_cont: Contact = Contact(ContType())
        test_firm.add_sb_firm(sub_firm)
        test_firm.add_sb_firm(sub_firm_2)
        test_firm.add_cont_to_sb_firm(test_cont)
        self.assertEqual(sub_firm.contacts[-1], sub_firm_2.contacts[-1])
        self.assertTrue(id(sub_firm.contacts[-1]) != id(sub_firm_2.contacts[-1]))

    def test_set_field(self):
        """ установка поля """
        firmFactory, lst_user_field = self.getSettingFirmFactory('firm1', 'Нижний Новгород')
        test: Firm = firmFactory.create()
        key = lst_user_field[0]
        old_value = firmFactory.usr_fields[key]
        new_value = "val_2"

        test.add_field(key, old_value)
        test.set_field(key, new_value)
        search_value = test.get_field(key)
        self.assertEqual(new_value, search_value)


if __name__ == '__main__':
    unittest.main()
