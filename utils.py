import random
from questions import QUESTION_BANK


#This function checks the lowercase version of the players answer against the lowercase version of the correct answer. 
def check_answer(player_answer, correct_answer):
    return player_answer.lower() == correct_answer.lower()


#This function calculates points for a trivia question. If the question difficulty was easy then you get 5 points.
# If the question difficulty was hard then you get 10 points. 
def calculate_points(difficulty):
    if difficulty == "easy":
        return 5
    else:
        return 10 

# This function determines the winner. If player 1's score was greater than player2's score then player 1 is the winner.
# If player 2's score was greater than player 1's score then player 2 is the winner. 
#If player 1 and player 2 scores equal each other then its a tie. 
def determine_winner(player1, player2):
    if player1.score > player2.score:
        return player1
    elif player2.score > player1.score:
        return player2
    

    else:
        return "Its a tie!"

