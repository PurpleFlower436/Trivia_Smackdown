import random
from questions import QUESTION_BANK



def calculate_points(player_answer, correct_answer ):
    """
    Compares the player's answer against the correct answer case-insensitively.

    Returns 10 points if the values match, and 0 points if they do not.

    :param player_answer: str representing the multiple-choice option selected by the user
    :param correct_answer: str representing the actual solution option key
    :return: int (10 for a match, 0 for a mismatch)
    """

    if player_answer.lower() == correct_answer.lower():
        return 10
    else:
        return 0
    


def determine_winner(player1, player2):
    """
    Evaluates the final scores of two players and determines the match outcome.

    Compares numeric scores and outputs a formatted victory announcement string 
    with the winning player's name and a trophy emoji, or a tie confirmation string.

    :param player1: Player instance representing the human user
    :param player2: Player instance representing the computer bot opponent
    :return: str announcing the explicit winner or a match tie condition
    """
    if player1.score > player2.score:
        return  player1.name + " " + "won!" + "🏆"
    elif player2.score > player1.score:
        return player2.name + " " + "won!" + "🏆"
    

    else:
        return "Its a tie!"



def is_valid_input(user_input):
    """
    Validates that a provided user input is a single character within the allowed options.

    Normalizes the input string to lower-case and checks if the length equals exactly 1 
    while confirming presence within options 'a', 'b', 'c', or 'd'.

    :param user_input: str collected directly from the active command-line prompt
    :return: bool (True if valid option, False otherwise)
    """
    cleaned_user_answer = user_input.lower()

    if len(cleaned_user_answer) == 1 and cleaned_user_answer in ["a", "b", "c", "d"]:
        return True
    else:
        return False



def load_questions(category, difficulty):
    """
    Retrieves a list of trivia question configurations from the centralized bank.

    Indexes dynamically into the QUESTION_BANK data resource structure using the 
    specified target grouping filters.

    :param category: str identifying the game topic (e.g., 'marvel', 'history')
    :param difficulty: str identifying the game target level (e.g., 'easy', 'hard')
    :return: list of dict instances, where each dict represents a standalone question object
    """


    questions = QUESTION_BANK[category][difficulty]

    return questions




    