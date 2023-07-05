from exercise import *



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

from server import app
app.execute_flask(port='1111')


