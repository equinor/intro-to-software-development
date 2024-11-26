import pytest

from rolling_stone.exceptions import InvalidPlayerNameException
from rolling_stone.player import Player


# Arrange
@pytest.fixture
def new_player():
    return Player()


def test_player(new_player):
    assert isinstance(new_player, Player)


def test_player_initial_score(new_player):
    assert new_player.score == 0


def test_player_receive_score(new_player):
    # Arrange
    RECEIVED_SCORE = 10
    assert new_player.score == 0

    # Act
    new_player.receive_score(RECEIVED_SCORE)

    # Assert
    assert new_player.score == RECEIVED_SCORE


def test_player_finished_game(new_player):
    RECEIVED_SCORE = 10
    new_player.receive_score(RECEIVED_SCORE)
    assert new_player.personal_best == 0

    new_player.finish_game()

    assert new_player.personal_best == RECEIVED_SCORE
    assert new_player.score == 0


def test_input_name_for_player(mocker, new_player):
    TEST_NAME = "Ola Nordmann"
    mocker.patch.object(
        Player, "_get_name_for_player_from_input", return_value=TEST_NAME
    )

    assert new_player.name is None

    new_player.prompt_for_name()
    assert new_player.name == TEST_NAME


@pytest.mark.parametrize(
    "invalid_name, exception_match_string",
    [
        ("", "Name must have at least one character"),
        ("123456789", "Name can only contain alphabetic characters and spaces"),
        ("NameWith@Symbol", "Name can only contain alphabetic characters and spaces"),
        ("Name With Too  Many   Spaces", "Name cannot have multiple spaces in a row"),
    ],
)
def test_input_invalid_name_for_player(
    mocker, new_player, invalid_name, exception_match_string
):
    mocker.patch.object(
        Player, "_get_name_for_player_from_input", return_value=invalid_name
    )

    with pytest.raises(InvalidPlayerNameException, match=exception_match_string):
        new_player.prompt_for_name()

    assert new_player.name is None
