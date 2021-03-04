
class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nation):
        players = self.reader.get_players()
        players = list(filter(lambda x: self.filterNationality(x, nation), players))
        players.sort(key = lambda p: p.points)
        players.reverse()
        return players

    def filterNationality(self, x, nation):
        if (x.nationality == nation):
            return True
        return False
