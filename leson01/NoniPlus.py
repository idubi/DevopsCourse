# get all numbers 
num_1 = int(input("Please enter a number:"));
num_2 = int(input("Please enter 2nd number:"));
num_3 = int(input("Please enter 3rd number:"));
#----------------------------------------------------------
#1# swap 2 first numbers with temp variable 
#----------------------------------------------------------
temp_swap = num_1;
 
num_1 = num_2;
num_2 = temp_swap;
print(f'num_1 = {num_1} , num_2 = {num_2}   ===> (1) , they are swapped' )

#----------------------------------------------------------
#2# write a program to swap 2 first numbers without a proxy : 
#----------------------------------------------------------
num_1,num_2 =num_2,num_1 
print(f'num_1 = {num_1} , num_2 = {num_2}  , ===> (2) ,  re-Swapped the numbers' )


#----------------------------------------------------------
#3# write a program to calculate sum of 2 numbers : 
#----------------------------------------------------------
print(f'sum of 2 first numbers is ===> (3)  : {num_1 + num_2} ' )

#----------------------------------------------------------
#4# write a program to get 3 numbers and get a pair equal if there is 
#----------------------------------------------------------
this_set = set()
this_set.add(num_1)
found = False
if num_2 in this_set:
    print(f'this item is more then once ====> (4): {num_2}')
    found = True
this_set.add(num_2)        
if num_3 in this_set:
    print(f'this item is more then once ====> (4): {num_3}')
    found = True
this_set.add(num_3) 
if not found : 
    print(f'there are no duplicates in this numbers ====> (4) : {this_set}')

#----------------------------------------------------------
#5# write a program to find smallest between 3 numbers
#----------------------------------------------------------
print(f'the smallest number is   ====> (5)  : {min(num_1,num_2,num_3)}')


#----------------------------------------------------------
#6# --> bonus ??? saw it in other people whatsup# 
#       write a program to calculate 2 first numbers cubes (power by 2): 
#----------------------------------------------------------
print(f'num_1 = {num_1} , num_2 = {num_2}  , ===> (6) qube sum is {num_2**2 + num_1**2}' )
 