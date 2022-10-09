# There are three types  of errors in python
# 1 syntax error
# print(we are learning python with Aammar) # SyntaxError: invalid syntax. Perhaps you forgot a comma?
# We need to add comma or quotes in order to remove this error.

# 2 Runtime error
print(25/0) #runtime error.

# 3 Semantic error (a human error and most dificult error to remove)
name="Aammar"
print("Hello name") # this will only show "Hello name".
print("Hello", name) # we must know where to add commas and quotes. 
# Sometimes we need no space between two words for that purpose we use + instead of ,. See example below.
print("Hello" + name)
