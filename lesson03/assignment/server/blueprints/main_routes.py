from flask import Blueprint, request, jsonify


# Create a Blueprint instance
main = Blueprint('main', __name__)


@main.route('/')
def index():
    return '<p>Hello from the file assignment , Class 03  ! </p><p> all api are on <b>/api/v1 </b> base route</[>'
