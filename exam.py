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
