"""
The Big Pig Game GUI Version
Aashish Panta 
September 6,2023
"""
import random 

def main():
    # print welcome message
    welcome_message()
    # initialize final player and computer value
    f_player = 0
    f_computer = 0
    # initialize the condition for the while loop to run game until there is a winner
    status=True 
    while status==True:
        # print dots & final scores of player and computer 
        dots_and_f_scores(f_player, f_computer)
        # initialize the current score of player and computer 
        c_player = 0
        c_computer = 0

        # while loop when user is playing
        while True:
            # ask user to roll or hold
            p_choice = roll_or_hold()
            if (p_choice == "r"):
                # roll the dice
                player_roll = dice_roll()
                # calcuate the score of dice roll
                p_score = score_compute(player_roll)
                if (p_score == 0):
                    c_player=0
                    c_score_print(player_roll,c_player,"player")
                    print("BIGPIG!!!!!!!!!!!!!!") 
                    break
                else:
                    c_player+=p_score
            else :
                break
            #print dice roll value and current score
            c_score_print(player_roll,c_player,"player")

         # update the final score
        f_player+=c_player     
         # print dots & final scores of player and computer 
        dots_and_f_scores(f_player, f_computer)

        # while loop when computer is playing
        while True:
            # ask choice of computer 
            c_choice=c_roll_hold(f_player,f_computer,c_computer)
            if (c_choice == "r"):
                # roll the dice
                comp_roll = dice_roll()
                # calcuate the score of dice roll
                c_score = score_compute(comp_roll)
                if (c_score == 0):
                    c_computer=0
                    c_score_print(comp_roll,c_computer,"computer")
                    print("BIGPIG!!!!!!!!!!!!!!") 
                    break
                else:
                    c_computer+=c_score
            else :
                break
            #print dice roll value and current score
            c_score_print(comp_roll,c_computer,"computer")

        # update the final score
        f_computer+=c_computer
        # print dots & final scores of player and computer 
        dots_and_f_scores(f_player, f_computer)
        # checks if the game needs to end or not, if yes, displays the winner 
        status=winner(f_player,f_computer)

def welcome_message():
    """
    print a welcome msg 
    Parameter: none
    Return: none
    Side effects: prints a welcome message and explains the game
    """
    print("* BIG PIG *")
    print("Welcome to Big Pig, the dice rolling game where players try to be the")
    print("first get 100 points! Players (you and the computer) will take turns")
    print("rolling two dice as many times as they want, adding all roll results to")
    print("a running total. Players lose their gained score for the turn if they")
    print ("roll a 1.")
    return

def dots_and_f_scores(f_player, f_computer):
    print("-----------------------------------------")
    print("Player has %i and Computer has %i" % (f_player,f_computer))

    return


def roll_or_hold():
    """
    prompts user to input a letter corresponding to choices about 
    what they will do in the game
    Parameter : none
    Returns: a string either "r" or "h"
    Side effects: none
    """
    while True:
        value=input("What do you want to do: [r]oll or [h]old? ")
        if value == "r" or value == "h":
            break
        else: 
            print("invalid value !!! Please enter either r or h")
    
    return value

def dice_roll():
    """
    rolls dice using random range
    Parameter : none
    Return : a list of two values   
    """

    dice1=random.randrange(1,7)
    dice2=random.randrange(1,7)
    list=[dice1,dice2]

    return list

def score_compute(rolls):
    """
    computes the score corressponding to the parameters
    Parameter: a list of two values
    Side effects : none 
    Return : an int which is the computed score

    """

    if rolls[0]==1 and rolls[1]==1:
        score=25
    elif rolls[0]==1 or rolls[1]==1:
        score=0
    elif rolls[0] == rolls[1]:
        score= 2 * (rolls[0]+rolls[1])
    else:
        score = rolls[0]+rolls[1]
    return score

def c_score_print(roll,score,str):
    print ("%s rolled [%i,%i], current round score: %i" % (str,roll[0],roll[1],score))
    return

def c_roll_hold(f_player,f_computer,c_computer):
    if f_player<100:
        if c_computer<20: 
            val="r"
        else:
            val="h"
    else:
        if f_computer <= f_player:
            val="r"
        else:
            val="h"
    return val


def winner(score1,score2):
    """
    checks if the game needs to end or not, if yes, displays the winner 
    Parameter: two int values which are the final score of player and computer 
    Return : a boolean either True or False 
    Side effect : print winner, and scores of both user and computer
    """
    if score1 >= 100 or score2 >= 100:
        if score1 > score2:
            print("Human wins [%i,%i)" % (score1,score2))
        else:
            print("Computer wins [%i,%i)" % (score1,score2))
        val=False
    else : 
        val=True      

    return val 

main()


