import pytest

@pytest.fixture
def sample_trivia_questions():

    return [  {
        "question": "What movie did Tony and Pepper get engaged in?",
        "choices": {
            "a": "Captain America Civil War",
            "b": "Avengers Age of Ultron",
            "c": "SpiderMan Homecoming",
            "d": "Iron Man 2"
        },
        "answer": "c"
    
    },
    
    {
        "question": "What is the movie where Tony Stark and Peter Parker meet for the first time?",
        "choices": {
            "a": "Captain America Civil War",
            "b": "Avengers Age of Ultron",
            "c": "Iron Man 3",
            "d": "Iron Man"
        },
        "answer": "a"
    },
    
    {
        "question": "What is the movie where Peter Parker meets Peter Parkers from alternate universes?",
        "choices": {
            "a": "Thor Ragnarok",
            "b": "Avengers Infinity War",
            "c": "Spiderman Far From Home",
            "d": "SpiderMan No Way Home"
        },
        "answer": "d"
    },
    
    ]
    
    
    
    