# More on Unit Testing

First, see [Intro to Unit Testing](../intro_to_unit_testing.md).

## 1. Getting started

If you have not done so already, follow the guides in [Exercise 0](0_working_environment.md) and [Exercise 1](1_setup_package_structure.md) to get started with the packaging structure.

We will build a small `Player` class for an imaginary game, driven entirely by tests.
The package path is `geo_calculator/rolling_stone/player.py`, so we need a subpackage.

- Create the source files (an `__init__.py` makes the folder an importable package):
  - `src/geo_calculator/rolling_stone/__init__.py` (can be empty)
  - `src/geo_calculator/rolling_stone/player.py`
- Create the test file `tests/rolling_stone/test_player.py`:

```python
from geo_calculator.rolling_stone.player import Player


def test_player() -> None:
    player = Player()
    assert isinstance(player, Player)
```

Run pytest with:

```
pytest
```

to verify that pytest runs, but that the new test fails.

Go on and implement the class and make the test pass.

## 2. Add score

Add a new test

```python
def test_player_receive_score() -> None:
    # Arrange
    player = Player()
    RECEIVED_SCORE = 10
    assert player.score == 0
    # Act
    player.receive_score(RECEIVED_SCORE)
    # Assert
    assert player.score == RECEIVED_SCORE
```

## 3. Add a fixture

We are testing the Player class and will need an instance of this in every test.
For this we can use a fixture and reuse it in all the tests. Add the following (remember
to `import pytest` at the top of the file):

```python
import pytest


@pytest.fixture
def new_player() -> Player:
    return Player()
```

A test that wants a fresh `Player` just takes `new_player` as an argument, and pytest
calls the fixture for you. Edit the previous tests to use it. For example like this:

```python
def test_player(new_player: Player) -> None:
    assert isinstance(new_player, Player)
    assert new_player.score == 0
```

## 4. Mock

Sometimes a unit talks to something we do not want to run in a test — user input, a network
service, a database, the current time. We can replace ("mock") that part so the test stays
fast, deterministic and isolated. Here we mock the private method that reads the player's
name from input, so the test never actually blocks waiting for a human.

Add 'pytest-mock' to dev dependencies in pyproject.toml and install the package again
with `pip install -e ".[dev]"`. This gives every test access to the `mocker` fixture.

Add a new test for `prompt_for_name()` on the class, but with a mocked service behind it:

```python
def test_input_name_for_player(mocker, new_player: Player) -> None:
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
```

## 5. Parametrize

It is often useful to run the same test, but with several cases. For this we can use
the decorator `@pytest.mark.parametrize`. The example below validates the player name and
expects a custom `InvalidPlayerNameException` to be raised for each bad input.

First define the exception (in `player.py`) and import it in the test:

```python
# In src/geo_calculator/rolling_stone/player.py
class InvalidPlayerNameException(Exception):
    pass
```

```python
# At the top of the test file
from geo_calculator.rolling_stone.player import InvalidPlayerNameException, Player
```

Then the parametrized test:

```python
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
    mocker, new_player: Player, invalid_name: str, exception_match_string: str
) -> None:
    mocker.patch.object(
        Player, "_get_name_for_player_from_input", return_value=invalid_name
    )
    with pytest.raises(InvalidPlayerNameException, match=exception_match_string):
        new_player.prompt_for_name()
    assert new_player.name is None
```

Run `pytest -v` and notice that each row above shows up as its own test case.

## Bonus

Add a test for what happens when a player finishes a game and implement it:

```python
def test_player_finished_game(new_player: Player) -> None:
    # Arrange
    # The player receives some score during the game

    # Act
    # The game is finished

    # Assert
    # If this was the highest personal score for the player, store this score
    # as a parameter for the player and consider resetting the score
```

Ideas to extend further:

- Add a `highscore` attribute and keep track of the best score across games.
- Use `pytest.approx` if you introduce any floating point scoring.
- Group the player tests in a class (`class TestPlayer:`) to organise them.
