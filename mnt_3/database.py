from abc import ABC, abstractmethod
import pymongo
from pymongo.server_api import ServerApi

import config

class BaseDatabase(ABC):
    @abstractmethod
    def save_account_data(self, account):
        pass

    # @abstractmethod
    # def get_accounts_uuids(self):
    #     pass

class FileStorage(BaseDatabase):
    ACCOUNT_STORAGE = 'account_storage.csv'
    TRANSACTION_STORAGE = 'transaction_storage.csv'
    SEPARATOR = '||'

    def save_account_data(self, account):
        with open(self.__class__.ACCOUNT_STORAGE, 'a') as account_storage:
            print(
                account.uuid,
                account.name,
                account.address,
                account.phone_number,
                account.secret_word,
                account.ssn,
                account.balance,
                account.credit_card,
                account.is_credit_allowed,
                account.created_at,
                account.deleted_at,
                sep=self.__class__.SEPARATOR,
                file=account_storage,
            )

    def get_accounts_uuids(self):
        with open(self.__class__.ACCOUNT_STORAGE, 'r') as account_storage:
            data_in_storage = account_storage.readlines()
            uuids = []
            for account in data_in_storage:
                uuids.append(account.split(self.__class__.SEPARATOR)[0])
            return uuids

    def get_account_data(self, uuid):
        with open(self.__class__.ACCOUNT_STORAGE, 'r') as account_storage:
            data_in_storage = account_storage.readlines()
            uuids = []
            for account in data_in_storage:
                if account.split(self.__class__.SEPARATOR)[0] == uuid:
                    data = account.split(self.__class__.SEPARATOR)
                    old_account_data = {
                    'uuid': data[0],
                    'name': data[1],
                    'address': data[2],
                    'phone_number': data[3],
                    'secret_word': data[4],
                    'ssn': data[5],
                    'balance': data[6],
                    'credit_card': data[7],
                    'is_credit_allowed': data[8],
                    'created_at': data[9],
                    'deleted_at': data[10],
                    }
                    return old_account_data



class MongoDBStorage(BaseDatabase):
    def __init__(self):
        client = pymongo.MongoClient(
            "mongodb+srv://admin:xQJFbVDywcFzb7zi@cluster0.ysycpfu.mongodb.net/?retryWrites=true&w=majority")

        self.db = client.account
        self.collection_accounts = self.db.accounts


    def save_account_data(self, account):
        new_account_data = {
            'uuid': account.uuid,
            'name':account.name,
            'address':account.address,
            'phone_number':account.phone_number,
            'secret_word':account.secret_word,
            'ssn':account.ssn,
            'balance':account.balance,
            'credit_card':account.credit_card,
            'is_credit_allowed':account.is_credit_allowed,
            'created_at':account.created_at,
            'deleted_at':account.deleted_at,
        }
        self.collection_accounts.insert_one(new_account_data)


storage_handler = MongoDBStorage()

assert isinstance(storage_handler, BaseDatabase)
