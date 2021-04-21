from flask import jsonify, request
from exceptions.resource_not_found import ResourceNotFound
from model.account import Account
from services.account_service import AccountService


def route(app):
    @app.route('/clients/<cl_id>/accounts', methods=['GET'])
    def get_account(cl_id):
        return jsonify(AccountService.all_account(int(cl_id))), 200

    @app.route('/clients/<cl_id>/accounts/<account_id>', methods=['GET'])
    def get_account_by_id(cl_id=None, account_id=None):
        try:
            account = AccountService.get_account_by_id(int(cl_id), int(account_id))
            return jsonify(account.json()), 200
        except ValueError as e:
            return 'Not a valid ID', 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/client/<client_id>/accounts', methods=['POST'])
    def post_account(cl_id):
        account = Account.json_parse_account(request.json)
        account.cl_id = int(cl_id)
        account = AccountService.create_account(account)
        return jsonify(account.json()), 201

    @app.route('/clients/<cl_id>/accounts/<account_id>', methods=['PUT'])
    def put_account(cl_id, account_id):
        account = Account.json_parse_account(request.json)
        account.account_id = int(account_id)
        try:
            AccountService.update_account(account)
            return jsonify(account.json()), 200
        except ValueError:
            print("Not Found")

    @app.route('/clients/<cl_id>/accounts/<account_id>', methods=['DELETE'])
    def del_account(cl_id, account_id):
        AccountService.delete_account(int(account_id))
        return '', 204

    @app.route("/client/<cl_id>/accounts?amountLessThan=2000&amountGreaterThan400", methods=['GET'])
    def get_account(account_balance):
        amount_less_than = request.args["amountLessThan"]
        amount_greater_than = request.args["amountGreaterThan"]
        if amount_less_than < account_balance < amount_greater_than:
            account = AccountService.get_account(int(account_balance))
        return jsonify(account), 200

