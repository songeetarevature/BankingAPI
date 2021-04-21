from daos.account_dao_impl import AccountDAOImpl


class AccountService:

    account_dao = AccountDAOImpl()

    @classmethod
    def create_account(cls, account):
        return cls.account_dao.create_account(account)

    @classmethod
    def all_account(cls, client_id):
        return cls.account_dao.all_account(client_id)

    @classmethod
    def get_account(cls, account_id):
        return cls.account_dao.get_account(account_id)

    @classmethod
    def get_account_by_id(cls, cl_id, account_id):
        return cls.account_dao.get_account_by_id(cl_id, account_id)

    @classmethod
    def update_account(cls, account):
        # add some logic
        return cls.account_dao.update_account(account)

    @classmethod
    def delete_account(cls, account_id):
        return cls.account_dao.delete_account(account_id)

    @classmethod
    def deposit(cls, deposit_amt):
        return cls.account_dao.update_account(deposit_amt)

    # @classmethod
    # def withdraw(cls, account_id):
    #     if 0 < cls.account_balance < cls.account_balance:
    #         account["account_balance"] -= account.account_balance    #
    #     return cls.account_dao.update_account(account_id)

    @classmethod
    def transfer_fund(cls, transfer_amt):
         cls.deposit(transfer_amt)

    @classmethod
    def get_specific_account(cls, account_balance):
        accounts = cls.all_account()
        refined_search = []
        for acc in accounts:
            if acc["account_balance"] <= account_balance:
                refined_search.append(acc)
        return refined_search
