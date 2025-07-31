from geo_calculator.rolling_stone.exceptions import InvalidPlayerNameException

class Player:
    def __init__(self):
        self.score = 0
        self.name = None

    def receive_score(self, score):
        self.score = score

    def _get_name_for_player_from_input(self):
        return input()

    def prompt_for_name(self):
        if self._get_name_for_player_from_input().__contains__(int):
            raise InvalidPlayerNameException.contains_ints
        if self._get_name_for_player_from_input() == "":
            raise InvalidPlayerNameException.empty
        if self._get_name_for_player_from_input().__contains__("@"):
             raise InvalidPlayerNameException.symbols
        if self._get_name_for_player_from_input().__contains__("  "):
             raise InvalidPlayerNameException.spaces
        
        self.name = self._get_name_for_player_from_input()


