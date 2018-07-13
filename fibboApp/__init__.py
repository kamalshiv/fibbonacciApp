from flask import Flask, jsonify, make_response

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # path to handle fibbonacci series request
    from . import fibbo
    app.register_blueprint(fibbo.bp)

    # Handle all invalid requests
    @app.errorhandler(404)
    def notFoundError(error):
        return make_response(jsonify({'error': 'Please check the url entered'}), 404)

    return app