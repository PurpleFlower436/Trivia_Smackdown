
#This is the player class which stores player info
class Player:
    def __init__(self, name):
        self.name = name #Player name
        self.score = 0 #The players initial score

    #The add_points function adds the points the player earned to their score 
    def add_points(self, points):
        self.score += points