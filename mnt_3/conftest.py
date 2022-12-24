import pytest
from faker import Faker
fake_data = Faker(locale='uk_UA')

from account import Account

@pytest.fixture(scope='session')
def account():
    new_account = Account(
        name=fake_data.name(),
        address=fake_data.address(),
        ssn=fake_data.ssn(),
        phone_number=fake_data.phone_number(),
        secret_word='12325'
    )
    yield new_account
