from player import Player

import random
import sqlalchemy

from utils import (
    
    calculate_points,
    determine_winner,
    load_questions,
    
  
)
from bots import choose_computer_bot_mode

from questions import QUESTION_BANK


"""

ask the user for their name
ask the user for the category and question difficulty

create player objects 1 for the user and the other for the computer
 -> if the user types in a category that is not in the categories list then we make them try again and type in the category
ask the user which bot they want to play against
load the questions up and shuffle them 
Iterate through the dictionary and have the user type in their answers
 then we call the calculate_points function which adds points to the players scores 
then we add scores to the sql alchemy database

once they reach 5 questions then you ask if you want to play again. if yes then we start again with a new category and difficulty level 
if no then we quit and show the final leaderboard at the end. 






"""


def newGame():
    print("Welcome to Trivia Smackdown!")
    print("You will have four categories to choose from: Marvel, World History, Pop Culture, and Disney World.")
    print("")
    print("You can choose between two levels, easy and hard, for each of the categories.")
    print("You will be asked to change categories or finish playing at the end of each game. The final scores will be revealed at the end.")
    print("")
    user_name = input(str("Enter your name player 1:"))

    p1 = Player(user_name)

    p2 = Player("Computer")


    user_decision = "Y"
    while user_decision == "Y":
        user_picked_category = input(str("What category do you want? Type in the letter to the corresponding category \n a. marvel, b. history, c. pop culture, d. disney:"))

        if user_picked_category not in ["a", "b", "c", "d"]:
            

            user_picked_category = input(str("What category do you want? Type in the letter to the corresponding category \n a. marvel, b. history, c. pop culture, d. disney:"))


        category_map = {
            "a":"marvel",
            "b":"history",
            "c":"pop_culture",
            "d":"disney",
        }

        question_category = category_map[user_picked_category]

        question_difficulty = input(str("Do you want easy or hard questions? Type in easy or hard:"))

        print("\Which computer bot mode do you want to play against?:")
        print("a) easy")
        print("b) medium")

        

        computer_bot_choice = input("Choose computer bot choice: ").lower()
    
        questions = load_questions(question_category, question_difficulty)


        for question in questions:
        
            print("\n" + question["question"] + "" + "\n")
            for key, value in question["choices"].items():
                print(key, value)


            computer_bot = choose_computer_bot_mode(computer_bot_choice, question)


            p1_answer = input(str("Enter your answer player 1:"))

            bot_answer = computer_bot

            player_1_score = calculate_points(p1_answer, question["answer"])

            player_2_score = calculate_points(bot_answer, question["answer"])

            p1.add_points(player_1_score)
            print("")

            print(p1.name, "current score:", p1.score)
            p2.add_points(player_2_score)
            print(p2.name, "current score:",p2.score)
        


        
        user_decision = input(str("Do you want to keep playing? Type in Y for Yes or Q to quit:"))
        

