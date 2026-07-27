from player import Player
import ui
import pandas as pd

import random
from sqlalchemy import select, desc
from leaderboard import score_leaderboard, update_leaderboard, initialize_leaderboard, engine
from utils import (
    calculate_points,
    determine_winner,
    load_questions,
    is_valid_input
)
from bots import choose_computer_bot_mode
from questions import QUESTION_BANK


def newGame():
    """
    Runs the main gameplay loop for Trivia Smackdown.

    This function controls the entire game flow from start to finish by running 
    these simple steps:
    1. Welcomes the player and explains the rules of Trivia Smackdown.
    2. Takes the player's name and sets up the scoreboard tracking.
    3. Starts a loop that lets the player keep playing new rounds until they decide to quit.
    4. Asks the player to select a question category, difficulty, and computer bot opponent.
    5. Loops through the trivia questions, making sure the player only inputs valid choices (a-f).
    6. Calculates round points, updates scores, and saves them to the leaderboard database.
    7. Declares the final match winner and prints out the updated standings table.

    :return: None
    """
    ui.show_title("Welcome to Trivia Smackdown!")
    ui.show_title("You will have four categories to choose from: Marvel, World History, Pop Culture, and Disney World.")
    print("")
    ui.show_title("You can choose between two levels, easy and hard, for each of the categories.")
    ui.show_title("You will be asked to change categories or finish playing at the end of each game. The final scores will be revealed at the end.")
    print("")

    
    user_name = input(str("Enter your name:"))

    p1 = Player(user_name)

    p2 = Player("Computer")

    initialize_leaderboard(p1.name, p1.score)
    initialize_leaderboard(p2.name, p2.score)
    
    user_decision = "Y"
    while user_decision == "Y":
        while True:
            print("")
            user_picked_category = input(str("What category do you want? Type in the letter that matches the corresponding category.\n" 
            " a. marvel, b. history, c. pop culture, d. disney: ")).lower()
          

            if user_picked_category in ["a", "b", "c", "d"]:
                break
            else:
                ui.show_error("Invalid category choice! Please enter a, b, c, or d for your category.")
            

        category_map = {
            "a":"marvel",
            "b":"history",
            "c":"pop_culture",
            "d":"disney",
        }

        question_category = category_map[user_picked_category]

        print("")
        question_difficulty = input(str("Do you want easy or hard questions? Type in easy or hard: "))


        print("")
        computer_bot_choice = input(str("Choose computer bot choice. Type in a for easy or b for hard: ")).lower()

        questions = load_questions(question_category, question_difficulty)


        for question in questions:

            ui.show_question(question)
            


            computer_bot = choose_computer_bot_mode(computer_bot_choice, question)

            while True:
                p1_answer = input(str("Enter your answer player 1:"))
                if is_valid_input(p1_answer):
                    break

                else:
                    ui.show_error("Invalid answer choice! Please enter a, b , c, or d. ")
            bot_answer = computer_bot

            player_1_score = calculate_points(p1_answer, question["answer"])

            player_2_score = calculate_points(bot_answer, question["answer"])

            p1.add_points(player_1_score)
            print("")
            update_leaderboard(p1.name, p1.score)
            
            p2.add_points(player_2_score)
            update_leaderboard(p2.name, p2.score)
            




        user_decision = input(str("Do you want to keep playing? Type in Y for Yes or Q to quit:"))


        winner = determine_winner(p1, p2)
        print("\n", winner)

        stmt = select(score_leaderboard)

        with engine.connect() as connection:
            df = pd.read_sql_query(stmt, connection)


        print("\n=======Current Leaderboard==========")
        print(df.to_string(index=False))



newGame()