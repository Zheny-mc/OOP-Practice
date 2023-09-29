from model import *
import unittest

class InitData:
    @staticmethod
    def create_list_firms() -> List[Firm]:
        with open('infoFirms.txt') as f:
            n = int(f.readline().rstrip())
            list_firm: List[Firm] = []
            for _ in range(n):
                obj = f.readline().rstrip().split()
                firm: Firm = Firm(
                    name=obj[0],
                    sh_name=obj[1],
                    country=obj[2],
                    region=obj[3],
                    town=obj[4],
                    street=obj[5],
                    postInx=obj[6],
                    date_in=obj[7],
                    email=obj[8],
                    web=obj[9]
                )
                list_firm.append(firm)
            # return len(lst_firm) == n
            return list_firm

    @staticmethod
    def create_list_contacts() -> List[Tuple[str, TypeContact]]:
        dct = {
            'f': ContTypeCol.F,
            's': ContTypeCol.S
        }

        with open('infoContacts.txt') as f:
            n = int(f.readline().rstrip())
            lst: List[Tuple[str, TypeContact]] = list()
            for i in range(n):
                obj = f.readline().rstrip().split()
                contact: TypeContact = FirmFactory.create_contact(name=obj[0], tpy=dct[obj[2]])
                contact.update({'note': obj[2], 'descr': obj[3], 'data_info': obj[4]})
                lst.append((obj[5], contact))
            return lst
            # return len(lst) == n

    @staticmethod
    def create_list_departments() -> List[Tuple[str, TypeDepartment]]:
        dct = {
            'f': DepartmentTypeCol.F,
            's': DepartmentTypeCol.S
        }

        with open('infoDepartments.txt') as f:
            n = int(f.readline().rstrip())
            lst: List[Tuple[str, TypeDepartment]] = list()
            for _ in range(n):
                obj = f.readline().rstrip().split()
                department = FirmFactory.create_department(obj[0], dct[obj[5]])
                lst.append((obj[6], department))
            return lst
            # return len(lst) == n

    @classmethod
    def create_full_lst_firms(cls) -> List[Firm]:
        lst_contact: List[Tuple[str, TypeContact]] = InitData.create_list_contacts()
        lst_department: List[Tuple[str, TypeDepartment]] = InitData.create_list_departments()
        lst_firm: List[Firm] = InitData.create_list_firms()

        for sh_name, dep in lst_department:
            dep_name = dep.get_name()
            for name, cont in lst_contact:
                if dep_name == name:
                    dep.add_contact(cont)

        for i in lst_firm:
            i_sh = i.get_sh_name()
            for sh_name, dep in lst_department:
                if i_sh == sh_name:
                    i.add_department(dep)

        return lst_firm


class SimplisticTest(unittest.TestCase):

    def test_find_firm_by_name(self):
        lst_firm: List[Firm] = InitData.create_full_lst_firms()
        self.assertTrue(len(ListFirm(lst_firm).find_by_name('Firms1')) == 1)

    def test_find_firm_by_country(self):
        lst_firm: List[Firm] = InitData.create_full_lst_firms()
        self.assertTrue(len(ListFirm(lst_firm).find_by_country('country_F1')) == 3)

    def test_add_contact_send_letter(self):
        '''Добавление контакта Письмо послали'''

        lst_firm: List[Firm] = InitData.create_full_lst_firms()
        lst = ListFirm(lst_firm).find_by_country('country_F1')
        contact = LetterSentContact('Письмо послали')

        res = [firm.add_cont(contact) for firm in lst]
        self.assertTrue(len(res) == 3)

    def test_add_contact_commerc(self):
        '''Добавление контакта коммерческое предложение'''
        lst_firm: List[Firm] = InitData.create_full_lst_firms()

        lst: List[Firm] = ListFirm(lst_firm).find_by_country('country_F1')
        contact = CommercialProposalContact('Коммерческое предложение')

        is_find_without_department: bool = True

        f = lambda arr: list(filter(lambda x: x.is_your_type() == DepartmentTypeCol.F, arr))

        result = []
        count_firm = 0
        for firm in lst:
            res = f(firm.get_all_department())
            if len(res) >= 1:
                count_firm += 1
                result.append(firm.add_cont_to_department(res[0], contact))
            else:
                if is_find_without_department:
                    if len(firm.get_all_department()) == 1:
                        count_firm += 1
                        result.append(firm.add_cont(contact))

        self.assertTrue(len(result) == count_firm)



if __name__ == '__main__':
    unittest.main()