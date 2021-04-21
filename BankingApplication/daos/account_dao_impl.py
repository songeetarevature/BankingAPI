from abc import ABC
from daos.account_dao import BankAppDAO
from exceptions.resource_not_found import ResourceNotFound
from model.account import Account
from util.db_connection import connection


class AccountDAOImpl(BankAppDAO, ABC):
    def create_account(self, account):
        sql = 'INSERT INTO account VALUES (DEFAULT, %s, %s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, (account.account_id, account.account_balance, account.cl_id))
        connection.commit()
        record = cursor.fetchone()
        new_account = Account(record[0], record[1], record[2])
        return new_account

    def all_account(self, cl_id):
        sql = 'SELECT * FROM account WHERE cl_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [cl_id])
        records = cursor.fetchall()
        account_list = []
        for record in records:
            account = Account(record[0], record[1], record[2])
            account_list.append(account.json())
        return account_list

    def get_account(self, client_id):
        sql = 'SELECT * FROM account WHERE cl_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        account_list = []
        for record in records:
            account = Account(record[0], record[1], record[2])
            account_list.append(account.json())
        return account_list

    def get_account_by_id(self, cl_id, account_id):
        sql = 'SELECT * FROM account WHERE cl_id = %s and account_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [cl_id, account_id])
        record = cursor.fetchone()
        return Account(record[0], record[1], record[2])

    def update_account(self, change):
        sql = 'UPDATE account SET account_balance = %s WHERE account_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [change.account_balance, change.account_id])
        #print("test")
        connection.commit()

    def delete_account(self, account_id):
        sql = 'DELETE FROM account WHERE account_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()





