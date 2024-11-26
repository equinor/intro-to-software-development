from rolling_stone.exceptions import InvalidPlayerNameException


class Player:
    def __init__(self):
        self.name = None
        self.score = 0
        self.personal_best = 0

    def _get_name_for_player_from_input(self):
        return input("Input player name: ")

    def receive_score(self, score):
        self.score += score

    def finish_game(self):
        if self.score > self.personal_best:
            self.personal_best = self.score
        self.score = 0

    def prompt_for_name(self):
        proposed_name = self._get_name_for_player_from_input()

        # The name
        # * must contain at least one character
        # * must have all characters alphabetic or spaces
        # * cannot have multiple spaces in a row
        if len(proposed_name) == 0:
            raise InvalidPlayerNameException(
                f"'{proposed_name}' is not a valid name. "
                "Name must have at least one character"
            )
        if not (all(c.isalpha() or c.isspace() for c in proposed_name)):
            raise InvalidPlayerNameException(
                f"'{proposed_name}' is not a valid name. "
                "Name can only contain alphabetic characters and spaces"
            )
        elif "  " in proposed_name:
            raise InvalidPlayerNameException(
                f"'{proposed_name}' is not a valid name. "
                "Name cannot have multiple spaces in a row"
            )
        else:
            self.name = proposed_name
