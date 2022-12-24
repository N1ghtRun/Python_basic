from uuid import uuid4
import hashlib
import random
import datetime
import time

import faker.providers.address
from faker import *

from database import storage_handler

credit_card_generator = Faker(locale='uk_UA')
address_generator = faker.providers.address.Provider



class Account:

    def __init__(self, **kwargs):
        self.name = credit_card_generator.name()
        self.address = '565777'
        self.ssn = 'fdsfa'
        self.phone_number = 'fadsfasf'
        self.secret_word = self.__class__.encrypt_data('fadfadfa')
        self.balance = 0
        self.credit_card = credit_card_generator.credit_card_full().split('\n')[2:4]
        self.uuid = str(uuid4())
        self.is_credit_allowed = random.choice([True, True, False])
        self.created_at = datetime.datetime.now().timestamp()
        self.deleted_at = None
        print(self.name)
        self.__save()

    def __str__(self):
        return f'Account {self.uuid} -> {self.name}. Balance: {self.balance}'


    @staticmethod
    def encrypt_data(value: str):
        encrypted_data = hashlib.md5(value.encode()).hexdigest()
        return encrypted_data

    def __save(self):
        storage_handler.save_account_data(self)

    @classmethod
    def get_uuids(cls):
        data = storage_handler.get_accounts_uuids()
        return {
            'uuids': data,
            'count': len(data),
        }

    @classmethod
    def restore_account(cls, uuid: str):
        old = storage_handler.get_account_data(uuid)
        old_account = cls(**old)

        old_account.balance = old['balance']
        old_account.uuid = old['uuid']
        old_account.created_at = old['created_at']
        return old_account



# data = Account.get_uuids()
# ob = Account.restore_account('1fd3e85c-57e0-444c-8616-3f01195fc9a4')
# print()
#
# import json
#
# data  = """{"uuid": "1fd3e85c-57e0-444c-8616-3f01195fc9a4", "name": "Охрім Скоробогатько"}"""
#
# n = json.loads(data)
# print(type(n))

for i in range(1000):
    Account()
    time.sleep(1)
