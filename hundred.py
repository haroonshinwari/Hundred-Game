'''Haroon SHINWARI -
This is a simple die game, where the objective is to score 100 by rolling a die. The computer starts first, and at each turn,
the computer or player depending on whose turn it is, must decide to either roll or not roll. They acumulate a score of whatever
they roll in one turn and it is added to their score, unless they roll a 1 in which case their cumulative score for that turn is 0,
and it is the other players turn. If a player chooses not to roll, his cumulative score for that turn is added to his total score.

Whoever gets to 100 first wins, however as the computer starts first,it has an advantage and therefore if the computer reaches 100,
the other player is given another turn, and whomever scores highest wins, if they are tied, they keep rolling until one gets a higher score.
'''


import random

def main():                                         #this is the fuction that will start the programme for execution

def rules():                                        #function for printing the rules and instructions for the player
    print("This is a simple die game with the objective to score 100 first.\nAt each turn you must choose to roll or not to roll.\nYou may roll as many times as you wish, and stop whenever you like.\nEverytime you roll you increase your cumulative score for that turn by the amount rolled.\nand this is added to your total score at the end of your turn.\nHowever if you roll a 1, your cumulative score for that turn goes to 0 and it is the next person’s turn.\n\nGiven the computer starts first, it has an advantage.\nTherefore you will have an extra turn if the computer reaches 100 first.\nThe winner is then decided by whoever has the highest score.\nIf it is tied then you keep rolling until whoever scores highest.") 
def human_move(computer_score, human_score):        #function to run when it is the human turn/move

def computer_move(computer_score, human_score):     #function to run when it is the computer's turn/move

def is_game_over(computer_score, human_score):      #function to determine whether there is a winner or not and if the game is over
      if (computer_score >= 100 or human_score >= 100) and computer_score != human_score:
        print('GAME OVER')
        return True
    else:
        print('not game over')
        return False
    
def roll():                                         #function to roll the die randomly        
    return random.randint(1,6)

def comproll():
    return random.randint(1,5)                      #function to decide if the computer rolls or not 

def ask_yes_or_no(prompt):                          #function to ask if the user would like to roll again or not 
    print(prompt)
    x = input()
    if x[0:1] == 'y' or x[0:1] == 'Y':
        print('True')
        return True
    elif x[0:1] == 'n' or x[0:1] == 'N':
        print('False')
        return False
def show_results(computer_score, human_score):      #function to show the results, who won and by how much when the game has ended
    if computer_score > human_score:
        cwin = computer_score - human_score
        print('Computer WINS! Computer wins by ' + str(cwin))
    elif human_score > computer_score:
        hwin = human_score - computer_score
        print('Player WINS! Player wins by ' + str(hwin))   

