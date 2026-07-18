import random
from questions import QUESTION_BANK






def calculate_points(player_answer, correct_answer ):

    if player_answer.lower() == correct_answer.lower():
        return 10
    else:
        return 0
    


def determine_winner(player1, player2):
    if player1.score > player2.score:
        return  player1.name + " " + "won!" + "🏆"
    elif player2.score > player1.score:
        return player2.name + " " + "won!" + "🏆"
    

    else:
        return "Its a tie!"



def is_valid_input(user_input):
    return user_input.isalpha()



def load_questions(category, difficulty):


    questions = QUESTION_BANK[category][difficulty]

    return questions




    