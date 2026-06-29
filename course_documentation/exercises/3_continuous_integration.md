# Setting up continuous integration with GitHub Actions

## Create workflow for GitHub Actions

As stated in the previous exercise, having tests in your code lets you make changes to the code base with confidence. When we want to commit our local work to the main code base, we want to make sure all our tests pass before we take in the changes. This can be done through a workflow running in GitHub Actions. In this exercise you will set up a workflow to run all the tests every time someone pushes to a pull request or to main.

> **Important:** GitHub requires the workflow file to already exist in the target branch
> (i.e. `main`) before it will run the workflow on pull requests targeting that branch.
> This means you need to merge a skeleton workflow into `main` first, and only then will
> the CI run when you open pull requests. The same rule applies whenever you add a new
> workflow later: merge its skeleton into the target branch before expecting it to trigger.

- Create a `.github/workflows/ci.yaml` file and build it up from top to bottom as follows:

  1. **Name** (optional but nice) — this is the label shown in the GitHub "Actions" tab:

     ```yaml
     name: CI
     ```

  2. **Triggers** — state when the workflow should run. We want it to run on every push to
     `main` and on every pull request targeting `main`:

     ```yaml
     on:
       push:
         branches:
           - main
       pull_request:
         branches:
           - main
     ```

  3. **Job definition** — name the job and choose the runner:

     ```yaml
     jobs:
       build:
         runs-on: ubuntu-latest
     ```

  4. **Steps** — list the individual steps the runner will execute. Start by checking out
     the code:

     ```yaml
         steps:
           - uses: actions/checkout@v5
     ```

  5. **Set up Python.** Enabling `cache: pip` reuses downloaded packages between runs,
     making the workflow faster:

     ```yaml
           - name: Set up Python 3.13
             uses: actions/setup-python@v5
             with:
               python-version: "3.13"
               cache: pip
     ```

  6. **Install dependencies** (including dev dependencies):

     ```yaml
           - name: Install dependencies
             run: |
               python -m pip install --upgrade pip
               pip install .[dev]
     ```

  7. **Run the tests:**

     ```yaml
           - name: Test with pytest
             run: |
               pytest
     ```

- Add this section to `pyproject.toml`:

  ```
  [project.optional-dependencies]
  dev = ["pytest"]
  ```

  - Note: This replaces the need for running `pip install pytest` and pytest is installed when we run `pip install .[dev]`

- Tip: run the exact same checks locally **before** pushing, for a much faster feedback loop than waiting for CI:

  ```bash
  pip install .[dev]
  pytest
  ```

## Commit, push and make a PR

- `git switch -c add-ci-workflow`
- `git add -p`
- `git add .github/workflows/ci.yaml`
- `git commit -m "Add ci workflow"`
- `git push origin add-ci-workflow`

- In GitHub, make a Pull Request from the `add-ci-workflow` branch to the `main` branch of your fork.

## Accept the PR

- Review your PR on GitHub.
- Notice the status check at the bottom of the PR — wait for it to go green before merging. You can click "Details" to watch the run in the Actions tab.
- Click the "Merge" button on GitHub
- Delete the branch on the remote origin (Press the button on GitHub)
- Delete the local branch
  - `git lg` to see the current shape of your history
  - `git fetch origin --prune` to update your local state of the remote
  - `git switch main` and `git rebase origin/main`
  - `git branch -d add-ci-workflow`

## Require the check to pass (branch protection)

Now that CI runs on every pull request, we can make GitHub enforce it so that nobody
(including you) can merge a PR while the tests are red.

- On GitHub, go to **Settings → Branches → Add branch ruleset** (or "Add rule") for `main`
- Enable **Require status checks to pass before merging** and select the `build` job
- Optionally enable **Require a pull request before merging** to block direct pushes to `main`
- Open a PR that intentionally breaks a test and confirm the "Merge" button is now blocked

# Bonus

The following sections might not be included in the course, depending on time, but we add it here for reference.

## Linting and code formatting with Ruff

While there are many freedoms in how you write your Python program, there are also style guides for how to write code consistently. The most renowned is [PEP8](https://peps.python.org/pep-0008/), written amongst others by the author of Python himself, Guido van Rossum.

For a long time the standard toolchain for enforcing this was a combination of separate tools: **Black** (formatter), **isort** (import sorter) and **flake8** (linter). Today, [Ruff](https://docs.astral.sh/ruff/) replaces all three. It is written in Rust, runs orders of magnitude faster, and is configured in one place.

Reference: the core difference is that formatters handle how your code looks, while linters handle how your code works. A formatter restructures visual elements like spacing, indentation, and line breaks without changing code behavior. A linter analyzes code structure to find potential bugs, security issues, and violations of programming best practices.

### Try it out

- Add `ruff` to your dev dependencies in `pyproject.toml`:

  ```toml
  [project.optional-dependencies]
  dev = ["pytest", "ruff"]
  ```

- Run `pip install .[dev]` to pick up the new dependency
- Run `ruff format --check .` to check formatting without changing files
- Run `ruff format .` to auto-format
- Run `ruff check .` to lint
- Run `ruff check --fix .` to auto-fix safe issues

### Configure Ruff in pyproject.toml

Add the following sections to `pyproject.toml`. This configures both the linter and the formatter:

```toml
[tool.ruff]
line-length = 127

[tool.ruff.lint]
ignore = ["E203", "E501", "E712"]
select = [
    "B",        # bugbear
    "E",        # pycodestyle
    "F",        # pyflakes
    "I",        # isort
    "PYI",      # flake8-pyi
    "UP",       # pyupgrade
    "RUF",      # ruff
    "W",        # pycodestyle
    "T10",      # flake8-debugger
    "PIE",      # flake8-pie
    "PGH",      # pygrep-hooks
    "PLE",      # pylint error
    "PLW",      # pylint warning
    "PLR1714",  # Consider merging multiple comparisons
]

[tool.ruff.lint.per-file-ignores]
"__init__.py" = ["F401"]

[tool.ruff.format]
docstring-code-format = true
line-ending = "lf"
```

Referece:

| Rule set | What it catches |
| B bugbear	| Likely bugs and bad practices (e.g. mutable default args, bare except) |
| W pycodestyle warnings	| Whitespace / style warnings (default only has errors) |
| I isort	| Unsorted/ungrouped imports |
| UP pyupgrade	| Outdated syntax (typing.List → list, str.format → f-strings, etc.) |
| T10	| Leftover breakpoint() / pdb calls |
| PGH	| Overly broad # type: ignore and # noqa comments |
| PIE	| Misc code simplifications |
| PLE/PLW/PLR1714	| Select pylint rules (redundant comparisons, etc.) |
| RUF	| Ruff-specific rules (unused noqa, ambiguous chars, etc.) |
| PYI	| Mostly relevant for .pyi stub files — less useful here |


### Add Ruff to the CI workflow

Add a new step to `ci.yaml` after the test step:

```yaml
      - name: Lint check
        run: |
          ruff check .

      - name: Format check
        run: |
          ruff format --check .
```

## Type hinting and type checking

- Type hints were introduced in Python 3.5 with [PEP484](https://peps.python.org/pep-0484/). The description states: "The proposal is strongly inspired by mypy", which is the tool we will be using to check type hinting.
- "Python is a dynamic language, so usually you'll only see errors in your code when you attempt to run it. Mypy is a static checker, so it finds bugs in your programs without even running them!" - https://mypy.readthedocs.io/en/stable/

- Run `mypy --help` for help text
- Run `mypy` or `mypy .` to check all your .py files in the current directory
- Extend the dev requirements in pyproject.toml to be `dev = ["pytest", "ruff", "mypy"]`
- Add a new section in pyproject.toml:

  ```toml
  [tool.mypy]
  exclude = ["build"]
  files = ["src", "tests"]
  ```

- Add the following step to `ci.yaml`:

  ```yaml
        - name: Type checking
          run: |
            mypy
  ```

- Add type hints to the `find_average` function.

  Hint: 
  ```def find_average(numbers: Sequence[int]) -> float:```

### Commit, push and observe the changes to the PR

- `git add -p`
- `git commit -m "Add linting and type checking"`
- `git push origin`

## Break the workflow

- Experiment with adding changes that break the tests, the formatting or the static type checking
- Try to think if the sequence of steps we run here makes sense, or something can be updated there?
