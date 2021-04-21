from abc import ABC, abstractmethod


class BankAppDAO(ABC):

    @abstractmethod
    def create_account(self, account):
        pass

    @abstractmethod
    def get_account(self, client_id):
        pass

    @abstractmethod
    def get_account_by_id(self, cl_id, account_id):
        pass

    @abstractmethod
    def all_account(self, cl_id):
        pass

    @abstractmethod
    def update_account(self, change):
        pass

    @abstractmethod
    def delete_account(self, account_id):
        pass
