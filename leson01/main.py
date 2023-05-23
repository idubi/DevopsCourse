#1. 
# (a)  
first = 7
# (b)
second = 44.3
# (c)
print ("1 ==> ")
print(f'...1.c ==> result sum of first & second --->  {first + second}')
# (d)
print(f'...1.d ==> result multiply of first by second ---> {first * second}')
# (e)
print(f'...1.e ==> result division of second by first---> {second / first}')

#2.
a = 8
a = 17
a = 9
b = 6
c = a+b
b = c+a
b = 8
print(f'2 ==> a={a}, b={b}, c={c}')
# result :
    # a=9
    # b=8
    # c=15


#3.
print ('3 ==> no , they both are ways to declare strings')

#4. 
my_number = 5+5
# print("result is: "+my_number)
# error : ---> TypeError: can only concatenate str (not "int") to str
# fix : 
print(f"4 ==> result is: {my_number}")

#5. 
x = 5
y = 2.36
print(f'5 ==>{x+int(y)}')


#6. 
a = 8
b = "123"
#   print(a+b)
#   fix (depends on expected result) : 
print ("6 (depends on expected result ) ==> ")
print(f'... ==> (1st solution) {a+int(b)}')
print(f'... 6 ==> (2nd solution) {a,b}')
print(f'... 6 ==> (3rd solution) {a}{b}')
