import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.players = []

        response = requests.get(url).json()

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['games']
            )

            self.players.append(player)

    def get_players(self):
        return self.players

