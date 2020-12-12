#Fibonacci cal and multipyer
#Made by Dark Murderer

#==============================================================================

import math

#==============================================================================

x=-2
y=2
i = 0
z = -1
list = []

#==============================================================================

n=int(input("enter your custom n:  "))

#==============================================================================

while i < n:
    z = abs(z - x)
    x = (x + z + y)
    o = x-z
    print(o)
    list.append(o)
    y = 0
    i += 1
print(list)

#==============================================================================

j = input("should we have zero in our calculation?y/n                 ")

if j == "y":
    m = list[0]
    for h in list[1:]:
        m = h * m
    print(m)
elif j == "n":
    m = list[1]
    for h in list[1:]:
        m = h * m
    print(m)
else:
    print("please try again and answer to the questions correctly!")
    pass

#==============================================================================