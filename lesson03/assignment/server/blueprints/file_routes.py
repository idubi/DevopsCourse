from flask import Blueprint

# Create a Blueprint instance
file = Blueprint('file', __name__)


@file.route('/')
def index():
    return 'Hello from the files blueprint!'
