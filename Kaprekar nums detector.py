#Kaprekar numbers detector made by Dark Murderer
#================================================
x = int(input("enter your non float number: "))
m = len(str(x)) - 1
y = x**2
i = 1
list = []
for o in str(y):
    list.append(o)
g = False
print(y)
if x >= 0:
    while g == False:
        k1 = []
        k2 = []
        li1 = list[:i]
        li2 = list[i:]
        for v in li1:
            k1.append(int(v))
        print(k1)
        for n in li2:
            k2.append(int(n))
        print(k2)
        d = 0
        for f in li1:
            d += 1
        s = 0
        for h in k1:
            d -= 1
            c = h * (10**d)
            s += c
        q = 0
        for lol in li2:
            q += 1
        w = 0
        for a in k2:
            q -= 1
            b = a * (10**q)
            w += b
        jvb = s + w
        if str(jvb) == str(x):
            g = True
        else:
            if i <= m:
                i += 1
            else:
                print("kaperkar nist")
                break
    else:
        print('kaperkar ast')
else:
    print("undefined number")
    pass
#================================================
