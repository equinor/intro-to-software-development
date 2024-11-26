# More on Unit Testing

First, see [Intro to Unit Testing](../intro_to_unit_testing.md).

## 1. Getting started

If you have not done so already, follow the guides in [Exercise 0](0_working_environment.md) and [Exercise 1](1_setup_package_structure.md) to get started with the packaging structure.

Create a file 'tests/rolling_stone/test_player.py'

```python
def test_player():
    player = Player()
    assert isinstance(player, Player)
```

run pytest with:

```
pytest
```

to verify that pytests runs, but that the new test fails.

Go on and implement the class and make the test pass.

## 2. Add score

Add a new test

```python
def test_player_receive_score():
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
For this we can use a fixture and reuse it in all the tests. Add the following:

```python
@pytest.fixture
def new_player():
    return Player()
```

and edit the previous tests to use this. For example like this:

```python
def test_player(new_player):
    assert isinstance(new_player, Player)
```

## 4. Mock

Sometimes we want to mock parts of the unit we are testing.

Add 'pytest-mock' to dev dependencies in pyproject.toml and install the package again
with 'pip install -e ".[dev]"'.

Add a new test for 'prompt_for_name()' on the class, but with a mocked service behind it

```python
def test_input_name_for_player(mocker, new_player):
    # Arrange
    TEST_NAME = "Ola Nordmann"
    mocker.patch.object(
        Player, "\_get_name_for_player_from_input", return_value=TEST_NAME
    )
    assert new_player.name is None

    # Act
    new_player.prompt_for_name()

    # Assert
    assert new_player.name == TEST_NAME
```

## 5. Parametrize

It is often useful to run the same test, but with several cases. For this we can use
the decorator `@pytest.mark.parametrize`

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
    mocker, new_player, invalid_name, exception_match_string
):
    mocker.patch.object(
        Player, "_get_name_for_player_from_input", return_value=invalid_name
    )
    with pytest.raises(InvalidPlayerNameException, match=exception_match_string):
        new_player.prompt_for_name()
    assert new_player.name is None
```

## Bonus

Add a test for what happens when a player finish a game and implement it

```python
def test_player_finished_game(new_player):
    # Arrange
    # The player receives some score during the game

    # Act
    # The game is finished

    # Assert
    # If this was the highest personal score for the player, store this score
    # as a parameter for the player and consider resetting the score
```
