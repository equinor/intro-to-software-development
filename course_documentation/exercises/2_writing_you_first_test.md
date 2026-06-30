# Writing your first test

## Add test

- Create /tests/test_calculations.py in VS code, or with:

  - `mkdir tests`
  - `cd tests`
  - `touch test_calculations.py`

- EXERCISE: In the `test_calculations.py`, write a test to test a find_average function that takes a list of numbers and returns the average. Assert that the returned average is correct. The find_average function does not yet exist, but that is intentional for now.

This is an example test that checks the length of a string:

```python
def test_length_of_string() -> None:
    test_string = "python"  # Arrange: set up the inputs
    length = len(test_string)  # Act: run the thing under test
    assert length == 6  # Assert: check the result
```

- A good test usually follows the **Arrange – Act – Assert** (AAA) structure, as annotated above. Keeping these three phases clearly separated makes tests easy to read. (See [intro_to_unit_testing.md](../intro_to_unit_testing.md) for more on test structure.)

- Start by importing the function you want to test from the relevant package in your module. `geo_calculator` is the package, `calculations` is the module and `find_average` is the function.
  (Hint: `from geo_calculator.calculations import find_average`)
- The module does not exist yet either — create `src/geo_calculator/calculations.py` so the import resolves.
- We have not implemented this function yet, so we expect the test to fail. But this is a good starting point for Test Driven Development. First, write the test. Second, run it and see that it fails. Third, implement the function so that the test passes. Finally, refactor your solution if needed.

## Install and run tests

- pip install pytest
- pytest
- See that the test fails
- Useful pytest flags while developing:
  - `pytest -v`: verbose output, one line per test
  - Read the failure trace carefully — pytest shows the exact assertion that failed and the values involved. Learning to read this red output is a core skill.
  - `pytest -k find_average`: run only tests whose name matches the expression (handy once you have many tests)
  - `pytest -x`: stop at the first failure

Hint: if you use VS Code, check your .vscode/settings.json and add the following lines if missing:
```json
{
    "python.testing.pytestArgs": [
        "tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```
This will enhance your experiance with VS Code's default Test Explorer when working with Pytest.

## Make test pass

- Up to you now...

## Reflections

- By adding tests to your code you get a lot of benefits:
  - You can verify that your code works as intended while you write it, at least the parts you manage to write tests for.
  - You can change parts of your code later with confidence, because you know you have tests that will tell you if you break something.
  - The tests serve as documentation for how you intend the code to be used.
- You can always write the tests later, but there are many benefits to writing them before you implement a single line of code:
  - You clarify the requirements before you start implementing.
  - It is more fun doing the implementation, because you know when you are done (the tests pass). It can even shorten the time it takes to write the implementation.
  - When the tests are written together with the implementation it makes life easier for the reviewers. They can start by reading the test to get a good first grasp of the problem at hand, and then look at the implementation.

## git commit

We will have another intro on what remotes are and how to work with them.

- Start by pushing your changes from the previous section
- `git push main`
- We typically don't want to push directly to main. It is up to each team to decide how to do this, but a common thing is to create pull requests (often from a personal fork to the main repository).
- Add branch protection on main branch.
- Commit your work. This time we will create a new branch and make a pull request
  - `git status`
  - `git switch -c implement-find-average`
  - `git add -p`: add changes in smaller patches / chunks / hunks
  - Manually add the untracked files with `git add <filename>`
  - `git commit -m "Implement find average"`
  - `git push origin implement-find-average`
- Create a Pull Request and click "Merge" when you think it looks correct.
- Click "Delete" on the branch that had the Pull Request.
- Clean up your local git environment
  - `git status`
  - `git log`, `git log --oneline`, `git lg`: The last one is an alias we created for you. It is compact, yet more extensive with information about other branches etc.
  - `git fetch origin --prune`, or `git fetch origin -p`
  - `git lg`: notice that the origin/implement-find-average branch is gone
  - `git rebase origin/main`: This will base the current branch on top of the remote main
  - `git lg`: notice that the current branch is based on origin/main now
  - `git switch origin/main` or (`git switch main` and `git rebase origin/main`)
  - `git branch -d implement-find-average`: We can finally delete the branch locally, knowing that it did not contain anything that was not already on origin/main.
  - `git lg`: verify that the local implement-find-average branch is gone
