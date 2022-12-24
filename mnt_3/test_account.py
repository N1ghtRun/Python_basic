class TestAccount:

    def test_new_account_money(self, account):
        assert account.balance == 0, 'Incorrect initial balance'
