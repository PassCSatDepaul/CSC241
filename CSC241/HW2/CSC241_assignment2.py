# CSC 241-401
# Assignment 2 template

# Put your name here

# List your collaborator(s) here (no more than two other people)

# Add a comment describing each person's contribution

# If you worked alone, add a comment indicating that

# Files without this information will earn a 0

# Include doc strings for full credit

# For each problem
#
#  
#  INPUT
#  variable name, source (user? passed in? file?), data type
#   
#
#  OUTPUT
#  variable name or input string, destination (screen? return? file?), data type 
#
#  PROCESSING (Algorithm or pseudocode)
#  Put your algorithm here for getting from the INPUT to the OUTPUT
#  
#
#  

# Question 1
def sequences():
    #This will get the desired output but each print will be a new line
    for x in range(27, 37):
        print(x)
    for x in range(21, 77, 7):
        print(x)
    for x in range(35, -1, -2):
        print(x)
    #if using python 2 this will allow them to be on the same line.
    #it has been commented out because I am running 3 and it doesn't let me run it. 
    #for x in range(27, 37):
    #    print x, 
    #for x in range(21, 77, 7):
    #    print x, 
    #for x in range(35, -1, -2):
    #    print x, 
    #If using python 3 this will allow them to be on the same line.
    #print statments are done because otherwise it keeps all print statments on the same line
    for x in range(27, 37):
        print(x, end = " ")
    print("\n")
    for x in range(21, 77, 7):
        print(x, end = " ")
    print("\n")
    for x in range(35, -1, -2):
        print(x, end = " ")
    
        

# Question 2
def returnThree(s):
    #works
    if len(s)>=3:
        print(s[0:3])
    else:
        print("' '")

# Question 3
def returnN(s, n):
    #works
    if len(s)>=n:
        print(s[0:n])
    else:
        print("' '")

# Question 4
def firstChars(lst):
    #works
    for x in lst:
        print(x[0:1])

# Question 5
def printGreater(nums, value):
    #works
    for i in nums:
        if i > value:
            print(i,end=' ')
