from exceptions.resource_not_found import ResourceNotFound
from model.client import Client
from services.client_service import ClientService
from flask import jsonify, request
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="test.log", level=logging.DEBUG, format=LOG_FORMAT, filemode="a")
logging.getLogger()
logging.info("Start")

def route(app):

    @app.route('/clients', methods=['GET'])
    def get_all_client():
        try:
            return jsonify(ClientService.all_client()), 200

        except ResourceNotFound as r:
            return r.message, 404

    logging.info("Get method - All clients")

    @app.route('/clients/<client_id>', methods=['GET'])
    def get_client(client_id):
        try:
            client = ClientService.get_client_by_id(int(client_id))
            return jsonify(client), 200
        except ValueError as e:
            return 'Not a valid ID', 400
        except ResourceNotFound as r:
            return r.message, 404

    logging.info("Get method - Specific client details retrieved")

    @app.route('/clients', methods=['POST'])
    def post_client():
        client = Client.json_parse_client(request.json)
        client = ClientService.create_client(client)
        return jsonify(client.json()), 201

    logging.info("Post method - New client created")

    @app.route('/clients/<client_id>', methods=['PUT'])
    def put_client(client_id):
        try:
            client = Client.json_parse_client(request.json)
            client.client_id = int(client_id)
            client = ClientService.update_client(client)
            return jsonify(client), 200
        except ValueError as e:
            return 'Not a valid ID', 400
        except ResourceNotFound as r:
            return r.message, 404

    logging.info("Put method - Update client")

    @app.route('/clients/<client_id>', methods=['DELETE'])
    def del_client(client_id):
        try:
            ClientService.delete_client(int(client_id))
            return '', 204
        except ValueError as e:
            return 'Not a valid ID', 400
        except ResourceNotFound as r:
            return r.message, 404

    logging.info("Delete method - Delete a client")
