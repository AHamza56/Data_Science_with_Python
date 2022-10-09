import string
x=10                # integer
y=10.2              # float
z="hello!"          # string

print(type(z))
# If we muliply a integer with float the class of integer will become float. See example below.
x= x*y
print(type(y)) # resul stated that it's a float. 

# Let's replace the values of x and y.
x=10.2 
y=10
y= x*y
print(type(y)) # float

# Let's add x and y and check the class
x=10
y=10.2
x=x+y
print(type(x)) # float 

# Implicit type conversion
print(x, "type of x is:" , type(x))

# Explicit type conversion
age=input("what is your age? ")
print(age)
print(type(age)) #results showing that class is string.

# We can change the class type by using int function.
age=input("what is your age? ")
age=int(age)
print(type(age)) # class has been changed to integer.
print(age, type (int(age))) # we can also use this method to convert float into integer.

# if we put our age 18.5 (float) in the output, this will be wrong. To overcome this we always use flot in the command.
print(age, type(float(age))) # class is float now.

# Name
name=input('What is your name? ')
print(name, type(string(name))) # class is string
#Let's replace string with integer
print(name, type(int(name)))  # Putting name (Ali) will show error because Ali is a string.
# In type conversions, we can change the type of our variables as per requirement. 



# Practice
age=input("what is your age?")
print(age, type(age))
# Class is string even we are putting integer. Let's change the class.
age=input("what is your age?")
print(age, type(int(age))) # class is integer

