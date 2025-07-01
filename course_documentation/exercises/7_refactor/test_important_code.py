import pytest

from important_code import old_legacy_function_that_is_very_important_but_nobody_remember_how_it_works

@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 0),
        (2, 0),
    ]
)
def test_important_code(n, expected):
    assert old_legacy_function_that_is_very_important_but_nobody_remember_how_it_works(n) == expected
