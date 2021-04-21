
def route(app):

    @app.route('/', methods=['GET'])
    def welcome():
        return 'Welcome to Your Bank'
