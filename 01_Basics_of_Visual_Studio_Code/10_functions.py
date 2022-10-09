# Defining a function

# First way to define a function
def print_codanics():
    print("we are learning python with Aammar")
    print("we are learning python with Aammar")
    print("we are learning python with Aammar") 
print_codanics()

# Second way to define a function
def print_codanics():
    text= "we are learning python with Aammar"
    print(text)
    print(text)
    print(text)
# We are learning python with Aammar has been published thrice. If changings are required simply make changes in text and all the lines will change.

# Third way to define a function
def print_codanics(text):
    print(text)
    print(text)
    print(text)
print_codanics("we are learning python with Aammar")

# Defining a function with if, elif and else statements
def school_calculator(age, text):
    if age==15:
        print("Ali can go to school")
    elif age>15:
        print("Ali should join higher school")
    else:
        print("Ali is still a young boy")
school_calculator(3, 'Ali')

# We can also use only age in the defining function but we have to give parameters, i.e., Ali can go to school.
def school_calculator(age):
    if age==15:
        print("Ali can go to school")
    elif age>15:
        print("Ali should join higher school")
    else:
        print("Ali is still a young boy")
school_calculator(3)

# Defining a function of future
def future_age(age):
    new_age=age+25
    return new_age
    print(new_age)
predicted_future_age= future_age(15)
print(predicted_future_age)

# Practice
from cgitb import text


def ali_hamza():
    print("We are learning python with Aammar")
    print("We are learning python with Aammar")
    print("We are learning python with Aammar")
ali_hamza()

def ali_hamza():
    text="we are learning python with Aammar"
    print(text)
    print(text)
    print(text)

def ali_hamza(text):
    print(text)
    print(text)
    print(text)
ali_hamza("we are learning python with Aammar")

def school_cal(age, text):
    if age==15:
        print("Ali can go to school")
    elif age>15:
        print("Ali should join higher school")
    else:
        print("Ali is still a young boy")
school_cal(11, "Ali")

def future_age(age):
    new_age=age+35
    return new_age
    print(new_age)
predicted_age_in_future=future_age(25)
print(predicted_age_in_future)
