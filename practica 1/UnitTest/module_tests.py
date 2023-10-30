import unittest
from models import *


class TestFirm(unittest.TestCase):

    def test_create_firm_factory(self):
        """ проверка правильности создания фирмы фабрикой """
        firm1: Firm = FirmFactory.create(name='firm1')
        firm2: Firm = Firm(name='firm1')
        self.assertEqual(firm1, firm2)

    def test_find_nizhny_novgorod_firms(self):
        """ правильность создания нижегородских фирм """
        firm1: Firm = FirmFactory.create(region='Нижний Новгород')
        firm2: Firm = FirmFactory.create(region='Нижний Новгород')
        firm3: Firm = FirmFactory.create(region='Москва')

        list_firms: FirmList = FirmList([firm1, firm2, firm3])
        result = list_firms.find('region', 'Нижний Новгород')
        self.assertEqual(len(result), 2)

    def test_add_to_sb_firm(self):
        '''добавление подразделения'''
        test: Firm = FirmFactory.create()
        new_sub: SubFirm = SubFirm()
        old_count: int = len(test.sb_firms)
        test.add_sb_firm(new_sub)
        new_count: int = len(test.sb_firms)
        self.assertEqual(old_count + 1, new_count)

    def test_addField(self):
        """ добавление поля """
        test: Firm = FirmFactory.create()
        key, value = "field_name", "val"
        test.add_field(key, value)
        search_value: str = test.get_field(key)
        self.assertEqual(value, search_value)

    def test_get_field(self):
        """ получение поля """
        test: Firm = FirmFactory.create()
        key, value = "field_name", "value"
        test.add_field(key, value)
        search_value = test.get_field(key)
        self.assertEqual(value, search_value)

    def test_rename_field(self):
        """переименовывание поля"""
        test: Firm = FirmFactory.create()
        old_key = "field_name_1"
        new_key = "field_name_2"
        value = "value"
        test.add_field(old_key, value)
        test.rename_field(old_key, new_key)
        search_value = test.get_field(new_key)
        self.assertEqual(value, search_value)

    def test_add_cont_to_sub_firm(self):
        """ добавление контакта к подразделениям """
        test_firm: Firm = FirmFactory.create()
        sub_firm: SubFirm = SubFirm()
        sub_firm_2: SubFirm = SubFirm()

        test_cont: Contact = Contact(ContType())
        test_firm.add_sb_firm(sub_firm)
        test_firm.add_sb_firm(sub_firm_2)
        test_firm.add_cont_to_sb_firm(test_cont)
        self.assertEqual(sub_firm.contacts, sub_firm_2.contacts)

    def test_set_field(self):
        """ установка поля """
        test: Firm = FirmFactory.create()
        key = "field_name"
        old_value = "val_1"
        new_value = "val_2"

        test.add_field(key, old_value)
        test.set_field(key, new_value)
        search_value = test.get_field(key)
        self.assertEqual(new_value, search_value)


if __name__ == '__main__':
    unittest.main()
