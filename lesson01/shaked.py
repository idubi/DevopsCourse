#1 


# number = "12234242"
# print("5" in number)


# num1 = 3
# num2 = 10
# num1 = num2
# num2 = num1
# print("num1 = ", num1, "num2 = ", num2)

# msg1 = "He" + "l"*2 +"o"
# msg2 = "world"
# print(msg1 , msg2)
# print(len(msg1+msg2))



# number = 123
# print(number // 100)
# print(number % 100 % 10) # ==> 3
# print(number % 10)


# number = 123
# print(number // 100)
# print(number % 100 // 10) # ==> 2
# print(number % 10)

#-----------------------------------------------------
#2 

# a=10
# b=15
# c=0
# #print(a % 2 ==(( c % 2 and b % 3) > a % 3))
# print(a != b and b != c)

#-----------------------------------------------------
#3 

# i = 1
# while i < 4:
#     print('wow')
#     i += 1


# for item in range (6):
#     if item % 2 == 1:
#         print(item * item)


# for item in range (9, 0, -3):
#     print (item)

# x = 5
# i = 1
# while i < 4:
#     x -= 1
#     i += 1
# print(i, x)


# Please enter a number:8128 

# def perfect_number():
#     num = int(input("Please enter a number:"))  # 28
#     sum = 0  # zero the accomulatoer
#     x = 1 
#     while x < num:
#         if (num % x == 0) :
#             sum = sum + x
#         x+=1
#     if (sum == num)  :
#         print("Perfect number ")
#     else:
#         print("Not perfect number ")
        
# perfect_number ()  




# def find_location ():
#     id_number = int(input("Please enter ID number:"))
#     digit = int(input("Please enter a digit:"))
#     found = False
#     for index in range(0,8):
#         if (id_number % 10 == digit):
#             print(index+1)
#             found = True
#         id_number = id_number // 10
#     if found == False:
#         print("-1")
# find_location()