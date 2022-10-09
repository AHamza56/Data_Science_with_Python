# There are two types of loop, i.e., While loops and For loops.

# While loop
x=0 #from where actually we want to start the value. If we put 1 then value will start from 1.
while (x<=100):
    print(x)
    x=x+1 #the purpose of writing x=x+1 is not to get infinite values. 
# While loop mean we are giving command that print until the value of x does not rearch to the value mentioned in tbe command, i.e., while (x<=100):

# For loop
for x in range(11,20):
    print(x)
# For loop always gives between values, i.e., 12-19.

# Array
days=("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
for d in days:
    print(d)

# We can also break and continue the loop by using "break" and "continue functions. See example below.
days=("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
for d in days:
    if (d=="Fri"):break #loop break
    print(d)
    if (d=="Fri"):continue #skips d
    print(d)

# Practice
x=5
while (x<=8):
    print(x)
    x=x+1

for x in range (11, 50):
    print(x)

days=("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
for d in days:
    print(d)
names=("Ali", "Hamza", "Akram", "Zeeshan", "Faizan", "Ibrahim", "Zain")
for n in names:
    # if (n=="Akram"):break
    # print(n)
     if(n=="Zeeshan"): continue
     print(n) 
