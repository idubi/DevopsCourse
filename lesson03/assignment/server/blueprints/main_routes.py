from flask import Blueprint, request, jsonify


# Create a Blueprint instance
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return 'Hello from the files blueprint!'
