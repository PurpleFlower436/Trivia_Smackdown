import random
def medium_bot(current_question):

    """
    Simulates a medium-difficulty opponent with a 70% accuracy threshold.
    
    Generates a random roll to choose between selecting the correct answer 
    (70% chance) or selecting a random incorrect answer (30% chance).

    :param current_question: dict containing the question string, choices, and correct answer
    :return: str representing the choice identifier ('a', 'b', 'c', or 'd') chosen by the bot
    """

    random_num = random.randint(1,100)

   
    all_choices = list(current_question["choices"].keys())

    correct_answer = current_question["answer"]

   
    if 1 <= random_num <= 70:
        
        return correct_answer

    
    else:

        filtered_answer_choices = [answer for answer in all_choices if answer != correct_answer]

        incorrect_answer = random.sample(filtered_answer_choices, 1)[0]

        return incorrect_answer



def easy_bot(current_question):

    """
    Simulates an easy-difficulty opponent that guesses completely at random.
    
    Selects a random answer identifier from all available keys in the choices list,
    disregarding what the correct answer actually is.

    :param current_question: dict containing the question string, choices, and correct answer
    :return: str representing the choice identifier ('a', 'b', 'c', or 'd') chosen by the bot
    """

   
   
    all_choices = list(current_question["choices"].keys())

    easy_bot_answer = random.choice(all_choices)

    return easy_bot_answer