import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_returns_a_player(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.__str__(), "Semenko EDM 4 + 12 = 16")

    def test_search_returns_None_if_no_such_player(self):
        player = self.statistics.search("Kukko Pärssinen")
        self.assertEqual(player, None)

    def test_team_search_returns_valid_team(self):
        team = self.statistics.team("PIT")
        self.assertEqual(team[0].__str__(), "Lemieux PIT 45 + 54 = 99")
    
    def test_top_scorers_first_is_the_most_points(self):
        scorers = self.statistics.top_scorers(1)
        self.assertEqual(scorers[0].points, 124)
        self.assertEqual(scorers[0].__str__(), "Gretzky EDM 35 + 89 = 124")
