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

def human_move(computer_score, human_score):        #function to run when it is the human turn/move

def computer_move(computer_score, human_score):     #function to run when it is the computer's turn/move

def is_game_over(computer_score, human_score):      #function to determine whether there is a winner or not and if the game is over

def roll():                                         #function to roll the die randomly        
    return random.randint(1,6)
def ask_yes_or_no(prompt):                          #function to ask if the user would like to roll again or not 

def show_results(computer_score, human_score):      #function to show the results, who won and by how much when the game has ended
    
