#this is a simple program to caculate your BMI

'''
made by Dark Murderer
ig = DarkMurderer_ggwp
telegram = DarkMurderer_ggwp
'''

#==============================================

def mohasebe():
    print("Your BMI is calculated.\nits ",BMI)

#==============================================

print("Welcome to BMI calculator\n[made by Dark Murderer]\n\n\nvaznetan ra vared konid(kg):")
w = float(input())
print("ghaddetan ra vared konid(m):")
H = float(input())


#==============================================

HT = H**2
BMI = (w/HT)

kamboodS = "kambood vazn shadid"
kambood = "kambood vazn khafif"
normal = "BMI normal"
Ezafe = "ezafe vazn"
CH1 = "chaghi daraje 1"
CH2 = "chaghi daraje 2"
CH3 = "chaghi daraje 3"

#==============================================

if BMI < 15:
    print("BMI shoma ", BMI , "ast. shoma " , kamboodS ,"darid")
elif BMI < 20 and BMI >= 15:
    print("BMI shoma ", BMI , "ast. shoma " , kambood ,"darid")
elif BMI < 25 and BMI >= 20:
    print("BMI shoma ", BMI , "ast. shoma " , normal ,"darid")
elif BMI < 30 and BMI >= 25:
    print("BMI shoma ", BMI , "ast. shoma " , Ezafe ,"darid")
elif BMI < 35 and BMI >= 30:
    print("BMI shoma ", BMI , "ast. shoma " , CH1 ,"darid")
elif BMI < 40 and BMI >= 35:
    print("BMI shoma ", BMI , "ast. shoma " , CH2 ,"darid")
elif BMI >= 40:
    print("BMI shoma ", BMI , "ast. shoma " , CH3 ,"darid")
else:
    print("adad vared shode sahih nist")

#==============================================

Parvande = {
    "Ghadd" : H,
    "vazn" : w,
    "BMI" : BMI
}

print("parvandeye shoma besharh zir ast:\n",Parvande)

#==============================================