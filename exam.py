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