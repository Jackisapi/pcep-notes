print(2**3)
# if both numbers are int reseult will be an int
print(2**3.0)
# if one value is a float the result will be a float
print(10/2)
#always returns a float
print(10 // 2)
#divides then rounds to the nearest lesser integer
print(4 % 3)
#returns the remander after the division
print(-2)
#- and - are special in that it can be used as a unary (one) operater to specify a number as negative or positive most operaters are binary (two) operators
print(2-2)

#the priority list goes +,- (unary) **m=, *, /, //, %.+ - (binary)
print(10-6**2/9*10+9)

print(2*(2+3))
#The only exception is when you use () to isolate an expression 

ammount_of_apples = 2 
cost_of_apple = 5
print(ammount_of_apples * cost_of_apple)
#Think of a variable like a container for data 
#variables must begin with letters or an _ no special charecters
#The name of a variable also cannot be a reserved keyword (think print)

cost_of_apple = cost_of_apple + 2 
#variables can be modified
cost_of_apple += 2 
#can also be modified

print("One Apple Costs " + str(cost_of_apple))
#A method to concat a sting to a variable

name = input("What is your name ")
''' Taking input name and storing it as string 
Inputs do not need prompts input() is also exceptable'''

truth = True

#conditional statements

if truth == True:
    #if this statement is true
    print("The Truth is True")
    #execute the following
else:
    #if it is not true 
    print("We have all been lied to")
    #execute this instead
#You can have multiple conditions using the elif statement
lies = False
if lies == True:
    print("Thats missinformation")
elif lies == False:
    print("Sounds about right")`

#string mutalation

#multiplying the ammount of times a string is displayed

print("ha"*10)

#However what happenes when you multiply a string by zero
print("ha" * 0)
#it will not be printed
#negative numbers?
print("ha" * -1)
#Same as zero 

#conataning strings 
print("this" + "that")

#comparison operaters

# == checks to see if two values are the same not to be confused with = which declares two things as the same

print(2==2)
print(2==4)

#!= checks to see if two valuse are NOT equal

print(2!=2)
print(2!=4)

# > checks to see if the value it is facing is greater than the value behind isolate
print(2 > 1)
print(1 > 2)

# >= checks to see if a value is greater than or equal to another value
print(2 >= 2)
print(2>=1)
print(1 >= 2)


# < less then checks to see if the value behind it is less then the value it is  facing 

print(4 < 2)
print(2 < 4)

# <= checks to see if two values are the same or if the value behind it is less than the value it is facing

print(4 <= 2)
print(2 <= 4)
print(2 <= 2)

#while loops 

# if the condition within the while loop is met the loop will continue to run 
i = 0
while(i != 10):
    print(i)
    i += 1 

#notice that once the condition is met the loop will stop running

#while loops can also except else statements

while(i != 20):
    print(i)
    i += 1
else:
    print("i is now " + str(i))

#for loops

for times in range(10):
    print("This loop has ran " + str(times) + " times")
#to stop the loop from running simply use a  break statements
    
for times in range(20):
    if(times == 15):
        print("Slow down there bud ")
        break

# if you want to skip a value simply use the continue statements

for times in range(10):
    if i == 3:
        continue
    print("This loop is at " + str(times))

#lists allow us to contian multiple elements

groceries = ["milk", "onions", "soda", "instant noodles"]
#NOTE In most programming languages including python lists start at zero NOT ONE in this example milk is in the position zero

print(groceries[0])
print(groceries[1])
print(groceries[2])
print(groceries[3])

#To change the value of an item in a list simply declare it like a variable

groceries[2] = 'mountian dew'
print(groceries[2])

# You can also get the length of the list using the len keyword (useful for loops and math)

len(groceries)

#to delete a item use the del keyword

del groceries[1]
#note this will remove that spot on the list shift all the items after the deleted item down

#To read through a list backwards use negative numbers starting at - 1 and going from there
print(groceries[-1])

#To add a new value to a list use append

groceries.append("Coffee")
#notice how the new value gets added on to the end of the list 
#to insert a value into a certian area on the list use this instead

groceries.insert(2,"Spagetti noodles")
                #position, data 
#to swap positions in the list simply do this

groceries[0], groceries[1] = groceries[1], groceries[0]

print(groceries)
#printing the list
for i in range(0,len(groceries)):
    print(groceries[i])

favorite_numbers = [12,5,8,6,2]
#to organize them simply use the .sort method (ONLY WORKS WITH INT AND FLOAT)
favorite_numbers.sort()
print(favorite_numbers)
#to reverse a list use the .reverse method
favorite_numbers.reverse()
groceries.reverse()
print(favorite_numbers)
print(groceries)

'''IMPORTIANT THING WITH lists
Say i have list parts
'''
parts = ['mobo','cpu','ram','psu']
print(parts)
#then I try to copy that list

componants = parts
print(componants)
'''This will cause python to use the same list for both keywords 
This is because when python sees this it will pull all the information from the same spot of memory
So if we delete an item from parts
'''

del parts[0]

print(parts)
print(componants)
#it will delete that item from both lists due to the fact that in memeory they are the same
drinks =['mntdew','pepsi','coffee']
#to copy a list you must splice it
sodas = drinks[:]
del sodas[2]
print(drinks)

print(sodas)
#Now they are seperate lists

#list slicing 

#as you could probably figure out list slicing works like this 
# list[start:end]
print(favorite_numbers[0:3])
#as you can assume you can store this as a variable 

top_three = favorite_numbers[0:3]

#if you dont include a number it will simply start at the first or last item in a list
print(top_three[:1])
print(top_three[:1])

#you can also use - values  to splice while removing certian values (useful if you dont know the length of a list)
print(favorite_numbers[1:-1])
#you can also delete items in a list with a slice (this will change the origional list)
del favorite_numbers[1:3]
print(favorite_numbers)

#finding items in a list
print(12 in favorite_numbers)
print(13 in favorite_numbers)
print(12 not in favorite_numbers)
print(13 not in favorite_numbers)
#this will return True or False and print it 
#2D matrix lists essencially lists within  a list
fridge = [
    ['cucumbers','tomatoes','celery'],
    ['cheese', 'ham','eggs'],
    ['milk','salami','soda']
]
print(fridge[2][0])

#3D matrix lists are lists within lists within lists

#Functions

def hello():
    print("Hello")
hello()
#To put it simply functions allow you to contain large ammounts of code and reuse them this makes your code easier to read and simply easier to write

#functions can take arguments think of these like variables 

def is_true(info):
    if info == True:
        print("this is true")
    else:
        print("This is false")
global_warming = False
is_true(global_warming)
global_warming = True
is_true(global_warming)

#You can also predefine arguments (these can still be changed as needed)

def sum(a=1,b=2):
    print(a + b)
sum()
sum(5,5)

#if you want to use your output in other chunks of your code you use the return statement. Observe

def is_true_two(info):
    if info == True:
        return True
    else:
        return false 
print(is_true_two(global_warming))
if is_true_two(global_warming) == True:
    print("Correct")
#Tuples

#tuples are simmilar to lists but with one major difference they are IMMUTABLEthis means that Tuples cannot be changed once they are creatled

fruits = {"apple","bannana","cherry"}

print(fruits)
