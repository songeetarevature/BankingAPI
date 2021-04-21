
class Account:
    def __init__(self, account_id=0, account_balance='', cl_id=0):
        self.account_id = account_id
        self.account_balance = account_balance
        self.cl_id = cl_id

    def json(self):
        return{
            'account_id': self.account_id,
            'account_balance': self.account_balance,
            'cl_id': self.cl_id,
        }

    @staticmethod
    def json_parse_account(json):
        account = Account()

        account.account_id = json['account_id'] if 'account_id' in json else 0
        account.account_balance = json['account_balance']
        account.cl_id = json['cl_id']
        return account

    def __repr__(self):
        return str(self.json())



