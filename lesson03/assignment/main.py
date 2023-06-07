from exercise import *

from flask import Flask
from lesson03.assignment.server.blueprints.main_routes import main
from lesson03.assignment.server.blueprints.file_routes import file

print_ex_boundary("ex01")
print(ex_01())
print_ex_boundary("ex02")
print(ex_02())
print_ex_boundary("ex03")
print(ex_03())
print_ex_boundary("ex04")
print(ex_04())
print_ex_boundary("ex05")
print(ex_05())
print_ex_boundary("ex06")
print(ex_06())
print_ex_boundary("ex07")
print(ex_07())
print_ex_boundary("ex10")
print(ex_10())


app = Flask(__name__)

# Register the blueprint with the app

app.register_blueprint(file, url_prefix='/file')
app.register_blueprint(main, url_prefix='/')

if __name__ == '__main__':
    app.run(port=30000)
