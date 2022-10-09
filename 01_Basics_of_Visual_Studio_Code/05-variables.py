# Variables: objects containing specific values.
x=14
print(x) # numeric or integer variable
y= 'i am learning python with full of my capacity' #string variable
print(y) # string variable
# Values of x or y can be changed depending upon the line numbers. See example below.
x=13 
print(x) 
y='python is so easy.'
print(y)
# Above results are different depending upon the commands used in different lines.
print(x+10) # adding the value of x present in line 8. if we want to use the value of x present in line 3 we can comment out the value of x present in line 8.

#types/class of variables
print(type(x)) # result stated that it's a <class 'int'>
print(type(y)) # result stated that it's a <class 'str'>

# Rules to assign a variable:
# 1- The variable should contain letters, number or underscores.
# 2- Do not start with numbers.
# 3- Never use spaces.
# 4- Do not use keywords used in fuctions (break, mean, median, test etc....).
# 5- Case sensitivity (always prefer lowercase letters).

fruit_basket='mangoes'
print(fruit_basket)
print(type(fruit_basket))
fruit_basket=8
print(fruit_basket)
print(type(fruit_basket))

# practice
x=56
print(x)
y="we are learning python"
print(y)
print(type(x))
print(type(y))
food_plate="biryani"
print(food_plate)
food_plate=8
print(food_plate)
print(type(food_plate))