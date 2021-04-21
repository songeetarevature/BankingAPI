from daos.client_dao import BankDAO
from exceptions.resource_not_found import ResourceNotFound
from model.client import Client
from util.db_connection import connection


class ClientDAOImpl(BankDAO):
    def create_client(self, client):
        sql = 'INSERT INTO client VALUES (DEFAULT, %s, %s, %s, %s, %s) RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, (client.client_first_name, client.client_last_name, client.client_email,
                             client.client_mobile, client.client_ssn))

        connection.commit()
        record = cursor.fetchone()
        new_client = Client(record[0], record[1], record[2], record[3], record[4], record[5])
        return new_client

    def get_client(self, client_id):
        sql = 'SELECT * FROM client WHERE id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])

        record = cursor.fetchone()

        if record:
            return Client(record[0], record[1], record[2], record[3], record[4], record[5]).json()
        else:
            raise ResourceNotFound(f'Client with id: {client_id} - Not Found')

    def all_client(self):
        sql = 'SELECT * FROM client'
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        client_list = []
        for record in records:
            client = Client(record[0], record[1], record[2], record[3], record[4], record[5])

            client_list.append(client.json())
        return client_list

    def update_client(self, change):
        sql = 'UPDATE client SET first_name=%s WHERE id = %s RETURNING *'
        cursor = connection.cursor()
        cursor.execute(sql, (change.client_first_name, change.client_id))

        record = cursor.fetchone()
        new_client = Client(record[0], record[1], record[2], record[3], record[4], record[5]).json()
        return new_client

    def delete_client(self, client_id):
        sql = 'DELETE FROM client WHERE id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()







