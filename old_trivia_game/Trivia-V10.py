#Trivia Game COMP 363 001 Final Project
#Bhargvi Handa and Amshah Mushtaq 

from operator import itemgetter
from re import A
import time
from playsound import playsound
import winsound
from  winsound import SND_LOOP


#instructions for players
print("")
print("Welcome to Trivia Smackdown!")
print("")
print("You will have four categories to choose from: Marvel, World History, Pop Culture, and Disney World.")
print("")
print("You can choose between two levels, easy and hard, for each of the categories.")
print("You will be asked to change categories or finish playing at the end of each game. The final scores will be revealed at the end.")
print("")
print("Grab a friend, and let's see who can get the most points!")
print("")

#dictionaries with questions and four answer choices per question

#dictionary filled with easy marvel trivia questions and their answer choices
Marvel_easy_questions = {
    "How many infinity stones are there?":[("a", "ten"), ("b", "six"),("c", "five"),("d", "two")],
    "In which Avengers movie do the Avengers first assemble?":[("e", "Avengers Infinity War"), ("f", "Avengers Age of Ultron"), ("g", "The Avengers"), ("h", "Avengers Endgame")],
    "What gift does Peter give MJ in Spider-Man Far From Home?":[("i", "notebook"),("j", "black dahlia bracelet"), ("k", "black dahlia necklace"), ("l", "drone")],
    "In Thor: Ragnarok, how long does Loki say he was falling for?":[("m", "thirty minutes"), ("n", "twenty minutes"), ("o", "forty minutes"), ("p", "ten minutes")],
    "What is the name of Thor's hammer?":[("q","Peggy"), ("r","Jonathan"), ("s","Storm Breaker"),  ("t","Mjolnir")]
}

#dictionary filled with hard marvel trivia questions and their answer choices
Marvel_hard_questions = {
    "Who said this line?: “I don’t know if you’ve been in a fight before, but there's usually not this much talking": [("a", "Peter Parker/Spider-Man"), ("b", "Bucky Barnes/The Winter Soldier"),("c","Steve Rogers/Captain America"), ("d", "Sam Wilson/The Falcon")], 
    "What is Morgan's first line in Avengers Endgame?:": [("e","Let’s go play"),("f","Define lunch or be disintegrated") ,("g","I am Iron Man"),("h","Hi Daddy")], 
    "In Spider-Man No Way Home, how does Peter trap Dr.Strange in the mirror dimension?": [("i","Peter webs Dr. Strange to a piece of the canyon"),("j","Peter uses his webs to create a archimedes spiral"),("k","Peter webs Dr. Strange to the train"), ("l", "Peter casts a spell that makes Dr. Strange fall through a portal")], 
    "Who said this line to Loki in the Disney+ series Loki?" "Your job is to help others become the best versions of themselves": [("m","Mobius"),("n","Ravonna Renslayer"), ("o","Sylvie"),("p","Hunter B-15")],
    "What does Tony tell Peter when he sees him being beamed up into Ebony Maw’s Q-ship?": [("q","You're too high up, you're running out of air"),("r","But you said save the wizard"),("s","Pete, you gotta let go I’m gonna catch you"), ("t", "Kid, where did you come from?")]
}

#This is a dictionary filled with easy world history questions and their answer choices
History_easy_questions = {
    "How many world wonders are there?": [("a","4"),("b","7"),("c","2"),("d","1")],
    "What is the tallest building in the world?": [("e","Willis Tower in Chicago"),("f","Burj Khalifa in Dubai"),("g","Shanghai Tower in China"),("h","One World Trade Center in New York City")],
    "When did World War I start?":[("i","1928"),("j","1901"),("k","1916"),("l","1914")],
    "Which country had the world’s first newspaper?": [("m","England"),("n","United States of America"),("o","China"),("p","Canada")],
    "Which is the largest country in the world based on population?": [("q","India"),("r","United States of America"),("s","China"),("t","Indonesia")]
}

#dictionary filled with hard world history questions and their answer choices
History_hard_questions = {
    "When was the United States Declaration of Independence signed?": [("a","October 15, 1776"),("b","June 19, 1775"),("c","August 2, 1776"),("d","April 9, 1777")],
    "What is considered the largest empire in history?": [("e","Han Dynasty"),("f","Mongol Empire"),("g","Ottoman Empire"),("h","Russian Empire")],
    "What was the name of the group formed to maintain world peace after WWI?": [("i","League of Legends"),("j","League of World Peace"),("k","League of Nations"),("l","League of Alliance")],
    "The Great Pyramid was built as a tomb for which pharaoh?": [("m","Khufu"),("n","Neferirkare Kakai"),("o","Userkaf"),("p","Sahure")],
    "How many languages are estimated to be spoken around the world?": [("q","8000"),("r","2500"),("s","500"),("t","7100")]
}

#dictionary filled with easy Disney World questions and their answer choices
Disney_World_easy_questions = {
    "When did Disney world open to the public?": [("a", "December, 1965"),("b", "August, 1980"), ("c", "October, 1971"),("d", "January, 1958")],
    "Who are the Fab 5?":[("e","Tinkerbell, Cinderella, Snow White, Peter Pan, and Fairy Godmother"), ("f","Mickey, Minnie, Donald, Goofy, and Pluto"), ("g","Mulan, Belle, Anna, Elsa, and Aurora"), ("h", "Captain Jack Sparrow, Mirabel, Mrs. Incredible, Captain America, and Loki")],
    "What is the smallest theme park at Disney World?":[("i", "EPCOT"), ("j","Disney's Animal Kingdom"), ("k", "Magic Kingdom"), ("l", "Hollywood Studios")],
    "What is the fastest ride at Disney World?":[("m","Test Track - 65 mph"), ("n","Rock ‘n’ Roller Coaster - 57pmh"), ("o","Summit Plummet - 60mph"), ("p","The Monorail - 55 mph")],
    "Which Disney park opened on Earth Day?":[("q", "Typhoon Lagoon"),("r", "Blizzard Beach"),("s","Magic Kingdom"), ("t", "Disney’s Animal Kingdom")]
}

#dictionary filled with hard Disney World questions and their answer choices
Disney_World_hard_questions = {
    "What is the biggest theme park at Disney World?":[("a", "Avengers Campus - 4 acres"), ("b","Epcot- 600 acres"), ("c","Disney’s Hollywood Studios - 154 acres"), ("d","Disney’s Animal Kingdom at 500 acres")],
    "How tall is Cinderella’s castle?":[("e","200ft"),("f","160ft"), ("g","400ft"), ("h","189ft")],
    "What are the three mountains called in Magic Kingdom?":[("i","Everest Mountain, Thunder Mountain, Slinky Dog Dash Mountain"), ("j", "Space Mountain, Splash Mountain and Big Thunder Mountain"), ("k","Expedition Everest, The Monorail Mountain, Splash Mountain"),("l","The Twlight Zone Tower of Terror, Tower Speedway, The Barnstormer")],
    "What is the maximum score you can get on Buzz Lightyear’s Space Ranger Spin?":[("m","1,000,000"),("n","600,000"),("o","100,000"),("p","999,999")],
    "How fast is the drop in Splash Mountain?":[("q","60 mph"), ("r","40 mph"), ("s","70mph"), ("t","200mph")]
}

#dictionary filled with easy Pop Culture questions and their answer choices
Pop_Culture_easy_questions = {
    "How many kids do Kim Kardashian and Kanye West have together?":[("a", "3"), ("b", "4"), ("c", "5"), ("d","2")],
    "How many Harry Potter books and movies are there?": [("e", "8 books and 9 movies"), ("f", "9 books and 8 movies"), ("g", "7 books and 8 movies"), ("h", "8 book and 7 movies")],
    "What is the name of Michelle Obama’s memoir written in 2018?": [("i", "Michelle Obama"), ("j", "Becoming"), ("k", "I am Michelle Obama"), ("l", "American Grown")],
    "What was the first non-English-language film to win Best Picture at the Oscars?": [("m", "Minari"), ("n", "Amour"), ("o", "Roma"), ("p", "Parasite")],
    "Who has the most Grammy awards?": [("q", "Georg Solti"), ("r", "Strevie Wonder"), ("s", "Quincy Jones"), ("t", "Jay-Z")]
}

#dictionary filled with hard Pop Culture questions and their answer choices
Pop_Culture_hard_questions = {
    "Who was named Forbes’ youngest self-made billionaire in 2019?": [("a", "Kylie Jenner"), ("b", "Austin Russell"), ("c", "Kevin David Lehmann"), ("d", "Katharina Andresen")],
    "How many Grammy Awards does Beyonce have?": [("e", "29"), ("f", "31"), ("g", "28"), ("h", "30")],
    "Which is the higest grossing film?": [("i", "Avatar"), ("j", "Avengers: Endgame"), ("k", "Titanic"), ("l", "Frozen II")],
    "How many million people watched the most viewed Super Bowl broadcast?": [("m", "110"), ("n", "112"), ("o", "111"), ("p", "114")],
    "Who is the person with the higest Instagram follower count?":  [("q", "Lionel Messi"), ("r", "Gigi Hadid"), ("s", "Cristiano Ronaldo"), ("t", "Selena Gomez")]
}


#dictionaries have the question numbers and their correct answers
Marvel_easy_questions_answers = {
    "1.": "b",
    "2.": "g",
    "3.": "k",
    "4.": "m",
    "5.": "t"
}

Marvel_hard_questions_answers = {
    "6.": "d",
    "7.": "f",
    "8.": "j",
    "9.": "m",
    "10.":"s"
}

History_easy_questions_answers = {
    "1.": "b",
    "2.": "f",
    "3.": "l",
    "4.": "o",
    "5.": "s"
}

History_hard_questions_answers = { 
    "6.": "c",
    "7.": "f",
    "8.": "k",
    "9.": "m",
    "10.": "t"
}

Disney_World_easy_questions_answers = {
    "1.":"c",
    "2.":"f",
    "3.":"k",
    "4.":"m",
    "5.":"t"
}

Disney_World_hard_questions_answers = {
    "6.":"d",
    "7.":"h",
    "8.":"j",
    "9.":"p",
    "10.":"r"
}

Pop_Culture_easy_questions_answers = {
    "1.": "b",
    "2.": "g",
    "3.": "j",
    "4.": "p",
    "5.": "q"
}

Pop_Culture_hard_questions_answers = {
    "1.": "a",
    "2.": "g",
    "3.": "i",
    "4.": "p",
    "5.": "s"
}


#chooseCategory function allows the player to pick which of the four categories they want, along with the difficulty level
#function also returns the questions, choices, and answers, which are used in the newGame function

def chooseCategory():
    
    #asks the player which category they want
    userCategory = input("Which category do you want? Marvel(a), World History(b), Pop Culture(c), or Disney World(d): ")
    userLevel = input("Do you want easy(a) or hard(b) questions?: ") #asks the player which difficulty level they want

    #based on the user's choice, the correct dictionaries are used in the newGame function
    if userCategory == "a" and userLevel == "a":
        #marvel and easy
        questions = Marvel_easy_questions.items() #questions from question dictionary 
        question_answer_pair = list(questions) #four answer choices from entries of the question dictionary 
        answers = Marvel_easy_questions_answers #answers from answer dictionary 
        return questions, question_answer_pair, answers #returns all values to be used to run each game
        
    if userCategory == "a" and userLevel == "b":
        #marvel and hard
        questions = Marvel_hard_questions.items()
        question_answer_pair = list(questions)
        answers = Marvel_hard_questions_answers
        return questions, question_answer_pair, answers

    if userCategory == "b" and userLevel == "a":
        #history and easy
        questions = History_easy_questions.items()
        question_answer_pair = list(questions)
        answers = History_easy_questions_answers
        return questions, question_answer_pair, answers

    if userCategory == "b" and userLevel == "b":
        #history and hard
        questions = History_hard_questions.items()
        question_answer_pair = list(questions)
        answers = History_hard_questions_answers
        return questions, question_answer_pair, answers
    
    if userCategory == "c" and userLevel == "a":
        #pop culture and easy
        questions = Pop_Culture_easy_questions.items()
        question_answer_pair = list(questions)
        answers = Pop_Culture_easy_questions_answers
        return questions, question_answer_pair, answers
    
    if userCategory == "c" and userLevel == "b":
        #pop culture and hard
        questions = Pop_Culture_hard_questions.items()
        question_answer_pair = list(questions)
        answers = Pop_Culture_hard_questions_answers
        return questions, question_answer_pair, answers
    
    if userCategory == "d" and userLevel == "a":
        #disney world and easy
        questions = Disney_World_easy_questions.items()
        question_answer_pair = list(questions)
        answers = Disney_World_easy_questions_answers
        return questions, question_answer_pair, answers
    
    if userCategory == "d" and userLevel == "b":
        #disney world and hard
        questions = Disney_World_hard_questions.items()
        question_answer_pair = list(questions)
        answers = Disney_World_hard_questions_answers
        return questions, question_answer_pair, answers

#newGame function allows players to play the games, decide if they want to keep playing, and start another round
#function consists of displaying the questions with answer choices, checking if the answer is correct, tracking points, and allowing new games
   
def newGame():
    
    #player names for player 1 and 2, which are used for entering answers and announcing final scores
    player_name = input("Player 1, Enter your name to get started: ")
    player2_name = input("Player 2, Enter your name to get started: ")
    
    #both players initially start with 0
    player_score = 0
    player2_score = 0

    userDecision = "Yes" #value of "Yes" to enter the game while loop

    while (userDecision == "Yes") or (userDecision == "yes") or (userDecision == "y"): #player chooses if they want to continue playing 
        questions, question_answer_pair, answers = chooseCategory()

        #this allows same questions to not be repeated once all five are answered 
        questionCount = 1
        while questionCount != 6: #five questions per each category (ex. history hard) 
            winsound.PlaySound("Kahoot_background_music.wav", winsound.SND_ASYNC |SND_LOOP |winsound.SND_ALIAS )
            
            question = question_answer_pair[0] #0 represents the question in the question dictionary 
            answer_choices = question_answer_pair[1] #1 represents five answer choices per each question 

            #make a loop for the questions 
            for question, answer_choices in questions: 
                print("")

                print(question) #question is show to the players along with the four answer choices 
                print("")
                print("Here are the answer choices:")
                print(answer_choices[0])
                print(answer_choices[1])
                print(answer_choices[2])
                print(answer_choices[3])
                print("")
                print("To enter your answers, please type in the letter that corresponds to the answer choice that you want.")
                player_answer = input("Enter you answer Player 1: ") #player 1 answers 
                player2_answer = input("Enter your answer Player 2: ") #player 2 answers 
                questionCount = questionCount + 1 #count is increased by 1, and the current question is not repeated

                for i in range(len(answers)): #pass in the dictionary of answer choices for the appropriate category
                    for i in answers: #loop through the answers dictionary 
                        if (player_answer == answers[i]): #check if the player answer matches the answer in the answers dictionary
                            player_score = player_score + 5 #player 1 gains 5 points
                            playsound("Correct_Answer_Sound.wav")

                        if (player2_answer == answers[i]): #check if player 2's answer matches the answer in the answers dictionary 
                            player2_score = player2_score + 5 #player 2 gains 5 points
                            playsound("Correct_Answer_Sound.wav")
                           
                        
                        #if a player's answer does not match the answers dictionary, they get zero points
                    print("")  
                    print(player_name + "'s Score: ") #both scored are shown to players
                    print(player_score) 
                    print(player2_name + "'s Score: ")
                    print(player2_score)
                    print("") 
                    break  

        #if Yes, game restarts
        #if No, game ends and final scores are revealed             
        print("Thank you for playing this category!")
        userDecision = input("Do you want to keep playing? (Yes) or (No): ")
        print("")

    if player_score > player2_score: #if player 1's score is greater than player 2's. if so, then player 1 is the winner!
        print("Congrats " + player_name + ", you are the winner!")
        print(player_name + "'s Final Score: ")
        print(player_score) 
        print(player2_name + "'s Final Score: ")
        print(player2_score)
        playsound('Victory_sound.wav')

    elif player_score < player2_score:  #if player 1's score is less than player 2, then player 2 is the winner
        print("Congrats " + player2_name + ", you are the winner!")
        print(player_name + "'s Final Score: ")
        print(player_score) 
        print(player2_name + "'s Final Score: ")
        print(player2_score)
        playsound('Victory_sound.wav')
    
    else:
        print("Congrats " + player_name + " and " + player2_name + "! You both are the winners!")    #if player 1 and 2's score tie, there both winners!
        print(player_name + "'s Final Score: ")
        print(player_score) 
        print(player2_name + "'s Final Score: ")
        print(player2_score)
        playsound('Victory_sound.wav') 

    
newGame()            