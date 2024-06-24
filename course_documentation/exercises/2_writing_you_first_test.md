# Writing your first test

## Add test

- Create /tests/test_calculations.py in VS code, or with:
- `mkdir tests`, `cd tests` and `touch test_calculations.py`

- In the `test_calculations.py` paste the following:

```python
from geo_calculator.calculations import find_average

def test_find_average_given_a_list_of_ints() -> None:
    numbers = [1, 2, 3, 4, 5, 6]
    assert find_average(numbers) == 3.5
```

- This is how you would typically write a simple test. Importing the function you want to test from the relevant package in your module. `geo_calculator` is the package, `calculations` is the module and `find_average` is the function.
- We have not implemented this function yet, so we expect the test to fail. But this is a good starting point for Test Driven Development. First, write the test. Second, run it and see that it fails. Third, implement the function so that the test pass. Finally, refactor your solution if needed.
- By adding tests to your code you get a lot of benefits:
  - You can verify that your code works as intended while you write it, at least the parts you manage to write tests for to.
  - You can change parts of your code later with confidence, because you know you have tests that will tell you if you break something.
  - The tests serves as documentation for how you intend the code to be used.
- You can always write the tests later, but there are many benefits to writing them before you implement a single line of code:
  - You clearify the requirements before you start implementing.
  - It is more fun doing the implementation, because you know when you are done (the test pass). It can even shorten the time it takes to write the implementation.
  - When the tests are written together with the implementation it makes the life easier for the reviewer. He or she can start with reading the test to get a good first grasp of the problem at hand, and then look at the implementation.

## Install and run tests

- pip install pytest
- pytest
- See that the test fails

## Make test pass

- Up to you now...

## git commit

- We typically don't want to push directly to main. It is up to each team to decide how to do this, but a common thing is to create pull requests (often from a personal fork to the main repository).
- Add branch protection on main branch.
- Only allow "Rebase and Merge".
- Commit your work. This time we will create a new branch and make a pull request
  - `git status`
  - `git checkout -b implement-find-average`
  - `git add -p`: add changes in smaller patches / chunks / hunks
  - Manually add the untracked files with `git add <filename>`
  - `git commit -m "Implement find average`
  - `git push origin implement-find-average`
- Create a Pull Request and click "Rebase and Merge" when you think it looks correct.
- Click "Delete" on the branch that had the Pull Request.
- Clean up your local git environment
  - `git status`
  - `git log`, `git log --oneline`, `git lg`: The last one is an alias we created for you. It is compact, yet more extensive with information about other branches etc.
  - `git fetch origin --prune`, or `git fetch origin -p`
  - `git lg`: notice that the origin/implement-find-average branch is gone
  - `git rebase origin/main`: This will base the current branch on top of the remote main
  - `git lg`: notice that the current branch is based on origin/main now
  - `git checkout origin/main` or (`git checkout main` and `git rebase origin/main`)
  - `git branch -d implement-find-average`: We can finally delete the branch locally, knowing that it did not contain anything that was not already on origin/main.
  - `git lg`: verify that the local implement-find-average branch is gone
