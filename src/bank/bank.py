import os

from .credit_dto import CreditContractDTO

cwd = os.getcwd()


class Bank:
    __bank_name = 'Банк Яблоко'
    __bank_city = 'Чита'
    __bank_responsible_person = 'начальник центра ипотечного кредитования Александрова Александра Александровича'
    __bank_address = 'г. Чита, ул. Выдуманная 25'
    __bank_correspondent_account = '78959595877'
    __bank_bik = '78986555'
    __bank_kpp = '78954524'
    __bank_inn = '787844555698'
    __bank_ogrn = '7878787879'
    __bank_email = 'yabloko@ya.ru'

    __credit_contract_template = os.path.join(cwd, 'src', 'bank', 'templates', 'credit_contract.docx')

    def __init__(self, scoring_model, printer):
        self.__scoring_model = scoring_model
        self.__printer = printer

    def print_credit_contract(self, dto: CreditContractDTO):
        self.__printer.print(self.__credit_contract_template, {
            'BANK_CITY': self.__bank_city,
            'BANK_NAME': self.__bank_name,
            'BANK_RESPONSIBLE_PERSON': self.__bank_responsible_person,
            'BANK_ADDRESS': self.__bank_address,
            'BANK_CORRESPONDENT_ACCOUNT': self.__bank_correspondent_account,
            'BANK_BIK': self.__bank_bik,
            'BANK_INN': self.__bank_inn,
            'BANK_KPP': self.__bank_kpp,
            'BANK_OGRN': self.__bank_ogrn,
            'BANK_EMAIL': self.__bank_email,
            'CLIENT_FULL_NAME': dto.client_full_name,
            'CLIENT_BIRTH_DATE': dto.client_birth_date,
            'CLIENT_ADDRESS': dto.client_address,
            'CLIENT_PASSPORT_SERIAL': dto.client_passport_serial,
            'CLIENT_PASSPORT_NUMBER': dto.client_passport_number,
            'CLIENT_PASSPORT_BY': dto.client_passport_by,
            'CONTRACT_NUMBER': dto.contract_number,
            'CONTRACT_PRICE': dto.contract_price,
            'CONTRACT_DURATION': dto.contract_duration,
            'CONTRACT_ACCOUNT': dto.contract_account,
            'CONTRACT_INTEREST_RATE': dto.contract_interest_rate
        }, os.path.join(cwd, 'src', '1.docx'))
