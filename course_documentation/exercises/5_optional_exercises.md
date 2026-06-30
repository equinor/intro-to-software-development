# Optional exercises or topics to cover

Here are some suggestions for exercises and topics if there is time left. Pick whatever
looks most interesting — they are independent of each other.

## Git

### Interactive rebase and rewriting history

- Make a few small commits on a branch, then run `git rebase -i origin/main`.
- Try `reword` (change a commit message), `squash` / `fixup` (combine commits) and
  reorder commits. This is how you clean up a messy branch before opening a PR.
- Combine `git commit --fixup <hash>` with `git rebase -i --autosquash` for a faster workflow.

### Cherry-pick

- Use `git cherry-pick <hash>` to copy a single commit from one branch onto another.
  Useful when one specific fix is needed elsewhere without merging a whole branch.

### Resolve a merge conflict on purpose

- Create two branches that change the same line of a file, merge/rebase one into the other,
  and practise resolving the conflict. Conflicts are normal — being comfortable resolving
  them is a valuable skill.

## Set up your own new GitHub repository

- Create a brand new repository from scratch and apply everything from the course:
  - Include `README.md`, `LICENSE` and `.gitignore`
  - Add a `pyproject.toml` and a small package under `src/`
  - Configure Pull Request settings (e.g. allow rebase merging)
  - Add branch protection to require a PR and passing CI before merging
  - Add a GitHub Actions workflow that runs `pytest` (and optionally Ruff / mypy)

## Tooling and quality

### Pre-commit hooks

- Install [pre-commit](https://pre-commit.com/) and add a `.pre-commit-config.yaml` that runs
  Ruff (and optionally mypy) automatically before each commit, so problems are caught locally
  before CI even runs.

### Test coverage

- Add `pytest-cov` to your dev dependencies and run `pytest --cov=geo_calculator`.
- Look at which lines are not covered by tests. Coverage is a useful signal, but remember:
  100% coverage does not guarantee correctness.

## More Python

### Classes and dataclasses

- Refactor a small piece of the package into a class, or try `@dataclass` to reduce boilerplate.
  (See [Exercise 6](6_more_on_unit_testing.md) for a class-based exercise.)

### Error handling

- Practise `try` / `except` / `finally` and raising your own custom exception classes.

### Type checking

- If you have not already, add `mypy` and resolve any type errors in your package
  (see the bonus section of [Exercise 3](3_continuous_integration.md)).
