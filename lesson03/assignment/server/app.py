from flask import Flask
from flask_cors import CORS
from blueprints.main_routes import main
from blueprints.file_routes import file


def execute_flask(port=30000, api_rout='/api/v1/'):
    app = Flask(__name__)
    cors = CORS(app)
    # cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Register the blueprint with the app

    app.register_blueprint(main, url_prefix=f'api_rout/')
    app.register_blueprint(file, url_prefix=f'{api_rout}file')

    if __name__ == '__main__':
        app.run(port=port)
