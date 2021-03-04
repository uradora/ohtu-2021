class Player:
    def __init__(self, name, team, nationality, assists, goals, penalties, games):
        self.name = name
        self.team = team
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.games = games
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20}" + self.team + " " + f"{str(self.goals):2}" + " " + f"{str(self.assists):2}" + " = " + str(self.points)
