#Rock,Paper,Scissors game
#made by Dark Murderer

import random

#===============================================================

moves = ["rock" , "paper" , "scissors"]
AI = 0
ct = 1
pw = aw = 0 
i = int(input("how many turns do you want to play?"))
while ct <= i:
    AI = random.choice(moves)
    print(moves)
    Player = str(input("Select your move: "))



    if Player in moves:
        pass
    else:
        print("undefined move, try again",moves)
        Player = str(input())



    if Player == "rock":
        if AI == "rock":
            print("tie!")
        elif AI == "paper":
            print("AI Wins!")
            aw = (aw+1)
        else:
            print("you Win!")
            pw = (pw+1)
            pass



    if Player == "paper":
        if AI == "paper":
            print("tie!")
        elif AI == "scissors":
            print("AI Wins!")
            aw = (aw+1)
        else:
            print("you Win!")
            pw = (pw+1)
            pass

        

    if Player == "scissors":
        if AI == "scissors":
            print("tie!")
        elif AI == "rock":
            print("AI Wins!")
            aw = (aw+1)
        else:
            print("you Win!")
            pw = (pw+1)
            pass



    else:
        pass

    ct += 1
    print("[P ",pw," : ",aw," AI]")

#===============================================================