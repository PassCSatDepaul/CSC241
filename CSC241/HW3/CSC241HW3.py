# CSC 241-401
# Assignment 3 template


# List your collaborator(s) here (no more than two other people)

# Add a comment describing each person's contribution


# Files without this information will earn a 0

# Include doc strings for full credit

# Question 1

def printMultiples(n, m):
    if n < 0 & m < 0:
        print()
    else:
        a= n
        b = m - 1
        #you do not need to add end it will still work
        #but by adding end you keep the values on the same level
        print(a, end = " ")
        for clock in range(0,b):
            n = a + n
            print(n, end = " ")
        

# Question 2

def customSpam(name, amount, address):
    
    space = name.find(" ")
    firstName = name[0:1].upper()+name[1:space]
    lastName = name[space+1:space+2].upper()+name[space+2:]
    upperAmmount = amount.upper()
    finishedAmmount = upperAmmount.replace("", " ")[1:-1]

    #name = name[:1].upper()+name[1:a]
    print('Dear '+ firstName +" "+ lastName)
    print('We would like to let you know about a great opportunity.')
    print('You can make '+ finishedAmmount + ' dollars in just a few short weeks!')
    print('This is a limited-time offer.')
    print('Please contact us at ' + address +' for more information')



    
    
        
# Question 3

def ion2e(s):
    if 'ion' in s[-3:]:
        s = s[0:-3]+ "e"
        print(s)
    else:
        print(s)

# Question 4
def numLen(s, n):
    clock = 0
    for word in s.split():
        if len(word) == n:
            clock += 1
    return clock

# Question 5
def makeNeg(lst, num):
    if len(lst) < num:
       print("The index is invalid")
    elif lst[num] < 0:
        print(lst)
    else:
        lst[num] =-lst[num]
        print(lst)
