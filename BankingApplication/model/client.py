
class Client:
    def __init__(self, client_id=0, client_first_name='', client_last_name='', client_email='', client_mobile='',
                 client_ssn=''):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.client_email = client_email
        self.client_mobile = client_mobile
        self.client_ssn = client_ssn

    def json(self):
        return{
            'client_id': self.client_id,
            'client_first_name': self.client_first_name,
            'client_last_name': self.client_last_name,
            'client_email': self.client_email,
            'client_mobile': self.client_mobile,
            'client_ssn': self.client_ssn
        }

    @staticmethod
    def json_parse_client(json):
        client = Client()

        client.client_id = json['client_id'] if 'client_id' in json else 0
        client.client_first_name = json['client_first_name']
        client.client_last_name = json['client_last_name']
        client.client_email = json['client_email']
        client.client_mobile = json['client_mobile']
        client.client_ssn = json['client_ssn']

        return client

    def __repr__(self):
        return str(self.json())
