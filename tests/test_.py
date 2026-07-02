import pytest 
from utils import check_answer, calculate_points, determine_winner, is_valid_input
from player import Player
from bots import medium_bot
import random



@pytest.mark.parametrize("user_input, expected",[
    ("A", True),
    ("b", True),
    ("495%%", False), 
    ("@", False),
    ("", False)
])


def test_is_valid_input(user_input, expected):
    assert is_valid_input(user_input) == expected

def test_check_answer():

    assert check_answer("A", "a") is True
    assert check_answer("495%%", "b") is False

def test_add_points():
    
    p1 = Player("Tony")

    p1.add_points(10)

    assert p1.score == 10

    p1.add_points(10)
    assert p1.score == 20


@pytest.mark.parametrize("p1_score, p2_score, expected_result", [
    (30, 20, "p1"), (10,25, "p2"), (20,20, "Its a tie!")
])


def test_determine_winner_scenarios(p1_score,p2_score,expected_result  ):
    p1 = Player("Tony")
    p2 = Player("Computer")

    p1.add_points(p1_score)
    p2.add_points(p2_score)

    result = determine_winner(p1, p2)

    if expected_result == "p1":
        assert result == p1
    elif expected_result == "p2":
        assert result == p2
    else:
        assert result == expected_result
  

