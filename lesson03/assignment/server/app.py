from flask import Flask
from flask_cors import CORS
from lesson03.assignment.server.blueprints import main_routes, file_routes


def execute_flask(port=30000, api_rout='/api/v1/'):
    app = Flask(__name__)
    CORS(app, supports_credentials=True)

    # Register the blueprint with the app
    app.register_blueprint(main_routes.main, url_prefix='/')
    app.register_blueprint(file_routes.file, url_prefix=f'{api_rout}file')

    if __name__ == 'server.app':
        app.run(port=port)
