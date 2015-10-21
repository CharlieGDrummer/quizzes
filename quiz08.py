def vectorial (x,y):
    
    lx = len(x)
    ly = len(y)
    if (ly != lx):
        r = "NaN"
        return (r)
    else:
        n = 0
        r = 0
        while ( n != lx): 
            r = r + (x[n]*y[n])
            n = n+1
        return (r)

#Two blank list
x=[]
y=[]


#In a real program, x and y would be lists given by the user
c = "y"

while (c == "y"):
    z = input ("Give me an integer for the FIRST set: ")
    x.append(z)
    c = input("Do you want to add more numbers to the set? Answer y for yes: ")
    c = c.lower()

c = "y"
    
while (c == "y"):
    z = input ("Give me an integer for the SECOND set: ")
    y.append(z)
    c = input("Do you want to add more numbers to the set? Answer y for yes: ")
    c = c.lower()

#Converts all members of the list to integers

l = len(x)
    
for e in range (0,l):
    x[e] = int(x[e])
    y[e] = int(y[e])
    
    
t = vectorial(x,y)

print ("The first list is: ",x)
print ("The second list is: "y)

print ("The result is: ", t)
