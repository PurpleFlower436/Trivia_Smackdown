import pytest 
from src.utils import  determine_winner, is_valid_input, calculate_points
from src.player import Player



@pytest.mark.parametrize("user_input, expected_result", [
    
    ("a", True),
    ("B", True),  
    ("c", True),
    ("D", True),
    
    
    ("495%%", False),  
    ("@", False),      
    ("1", False),      
    ("abc", False),    
    ("", False),       
    (" ", False)       
])
def test_is_valid_input_scenarios(user_input, expected_result):
    """Verifies that is_valid_input only approves single valid choice letters (A-D)."""
    assert is_valid_input(user_input) == expected_result









@pytest.mark.parametrize("player_answer, correct_answer, expected_points", [
    ("c", "c", 10),
    ("B", "b", 10),
    ("a", "c", 0),
    ("495%%", "c", 0),
    ("", "c", 0)
])

def test_calculate_points_scenarios(player_answer, correct_answer, expected_points):

    assert calculate_points(player_answer, correct_answer) == expected_points




def test_add_points():
    
    p1 = Player("Tony")

    p1.add_points(10)

    assert p1.score == 10

    p1.add_points(10)
    assert p1.score == 20


@pytest.mark.parametrize("p1_score, p2_score, expected_result", [
    (30, 20, "Tony won!🏆"), (10,25, "Computer won!🏆"), (20,20, "Its a tie!")
])


def test_determine_winner_scenarios(p1_score,p2_score,expected_result  ):
    p1 = Player("Tony")
    p2 = Player("Computer")

    p1.add_points(p1_score)
    p2.add_points(p2_score)

    result = determine_winner(p1, p2)

    assert result == expected_result
