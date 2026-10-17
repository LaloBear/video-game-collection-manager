import json
from video_game import VideoGame

class GameManager:
    def __init__(self):
        self.games = []

    def add_game(self, game):
        for g in self.games:
            if g.name.lower() == game.name.lower():
                return False
            
        self.games.append(game)
        return True

    def search_game(self, name):
        for g in self.games:
            if g.name.lower() == name.lower():
                return g

        return None

    def remove_game(self, name):
       game = self.search_game(name)

       if game is None:
           return False

       self.games.remove(game)
       return True

    def mark_game_finished(self, name):
        game = self.search_game(name)

        if game is None:
            return False

        return game.mark_finished()

    def rate_game(self, name, rating):
        game = self.search_game(name)

        if game is None:
            return False

        return game.rate_game(rating)

    def get_games_by_platform(self, platform):
        matching_games = []

        for g in self.games:
            if g.platform.lower() == platform.lower():
                matching_games.append(g)

        return matching_games

    def get_finished_games(self):
        matching_games = []

        for g in self.games:
            if g.finished:
                matching_games.append(g)

        return matching_games

    def get_unfinished_games(self):
        matching_games = []

        for g in self.games:
            if not g.finished:
                matching_games.append(g)

        return matching_games

    def get_games_sorted_by_name(self):
        return sorted(self.games, key=lambda g: g.name.lower())

    def view_all_games(self):
        return self.games

    def save_games(self):
        games_data = []

        for game in self.games:
            game_data = {
                "name": game.name,
                "release_year": game.release_year,
                "developer": game.developer,
                "platform": game.platform,
                "finished": game.finished,
                "rating": game.rating
            }

            games_data.append(game_data)

        with open("games.json", "w") as file:
            json.dump(games_data, file, indent=4)

    def load_games(self):
        try:
            with open("games.json", "r") as file:
                games_data = json.load(file)
        except FileNotFoundError:
            return

        for game_data in games_data:
            game = VideoGame(
                game_data["name"],
                game_data["release_year"],
                game_data["developer"],
                game_data["platform"]
            )
            game.finished = game_data["finished"]
            game.rating = game_data["rating"]

            self.games.append(game)