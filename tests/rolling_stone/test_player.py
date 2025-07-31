from geo_calculator.rolling_stone.player import Player
from geo_calculator.rolling_stone.exceptions import InvalidPlayerNameException
import pytest

def test_player():
    player = Player()
    assert isinstance(player, Player)

def test_player_receive_score():
    # Arrange
    player = Player()
    RECEIVED_SCORE = 10
    assert player.score == 0
    # Act
    player.receive_score(RECEIVED_SCORE)
    # Assert
    assert player.score == RECEIVED_SCORE

@pytest.fixture
def new_player():
    return Player()

def test_player(new_player):
    assert isinstance(new_player, Player)
    assert new_player.score == 0

def test_input_name_for_player(mocker, new_player):
    # Arrange
    TEST_NAME = "Ola Nordmann"
    mocker.patch.object(
        Player, "_get_name_for_player_from_input", return_value=TEST_NAME
    )
    assert new_player.name is None

    # Act
    new_player.prompt_for_name()

    # Assert
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