class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.over_3_points = False
    
    def won_point(self):
        self.points += 1
        if self.points >= 4:
            self.over_3_points = True

    def get_score(self):
        return self.points

    def get_name(self):
        return self.name

    def get_over_3_points(self):
        return self.over_3_points

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.winning = None

    def won_point(self, player_name):
        diff = self.get_absolute_diff()

        if player_name == self.player1.name:
            self.player1.won_point()
        else:
            self.player2.won_point()
        if self.winning == None or diff == 0:
            self.winning = player_name

    def get_score_names(self, score):

        scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }

        return scores[score]

    def get_absolute_diff(self):
        return abs(self.player1.get_score() - self.player2.get_score())

    def advantage_or_win(self, diff):
        if diff == 1:
            return "Advantage " + self.winning
        else:
            return "Win for " + self.winning

    def get_score(self):

        diff = self.get_absolute_diff()

        if self.player1.get_over_3_points() or self.player2.get_over_3_points():
            if diff == 0:
                return "Deuce"
            else:
                return self.advantage_or_win(diff)
        else:
            score1 = self.player1.get_score()
            score2 = self.player2.get_score()
            if diff == 0:
                return self.get_score_names(score1) + "-All"
            else:
                return self.get_score_names(score1) + "-" + self.get_score_names(score2)
