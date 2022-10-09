# Logical operators are either "True or False" or "Yes or No" or "0 or 1"
# equal to                          ==
# not equal to                      !=
# greater than                      >
# less than                         <
# greater than or equal to          >=
# less than or equal to             <=

# is 4 equal to 4?
print(4==4) #true is the answer
# is 4 greater than 5?
print(4>5) #false
# is 4 is less than or equal to 5
print(4<=5) #true
# is 4 not equal to 5?
print(4!=5) #true

# Applications of conditional logics
ali_age=4
minimum_age_at_school=5
print(ali_age==minimum_age_at_school)

# Input functions and logical operators
minimum_age_at_school=5
ali_age=input("how old is Ali? ") # input fucntion
ali_age=int(ali_age)
print(minimum_age_at_school==ali_age) # logical operator

# Practice
print(4==4)
print(4>3)
print(4>=3)
hamad_age=5
age_at_school=6
print(hamad_age==age_at_school)
hamad_age=input("what is you age? ") # input function
hamad_age=int(hamad_age)
print(age_at_school==hamad_age)      # logical operator

age_required_for_signup=18
your_age=input("What is your age? ")
your_age=int(your_age)
greetings="welcome to netflix"
print(greetings, age_required_for_signup==your_age)