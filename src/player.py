class Player:
    """
    Represents a competitor in the trivia game to track identity and score progression.
    """
    def __init__(self, name):
        """
        Initializes a new player profile with a name and a clean scoring slate.

        :param name: str representing the player's identity or alias
        """
        
        self.name = name 
        self.score = 0 

    
    def add_points(self, points):
        """
        Increments the player's cumulative game score by a specified value.

        :param points: int value representing the point payload earned during a round
        :return: None
        """
        self.score += points

    