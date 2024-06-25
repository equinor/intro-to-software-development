# Setting up continuous integration with GitHub Actions

## Create workflow for GitHub Actions

- As stated in the previous exercise, having tests in your code lets you make changes to the code base with confidence. When we want to commit our local work to the main code base, we want to make sure all our tests pass before we take in the changes. This can be done through a workflow running in GitHub Actions. In this exercise you will set up a workflow to run all the tests every time someone pushes to a pull request or to main.

- Create a .github/workflows/ci.yaml file and past the following:

  - First, checkout the code:

    ```yaml
    jobs:
      build:
        runs-on: ubuntu-latest

        steps:
          - uses: actions/checkout@v4
    ```

  - Then, setup Python with the right version

    ```yaml
    ...
      ...
        ...
          - name: Set up Python 3.10
            uses: actions/setup-python@v5
            with:
              python-version: "3.10"
    ```

  - Then, install dependencies (including dev dependencies):

    ```yaml
    ...
      ...
        ...
          - name: Install dependencies
            run: |
              python -m pip install --upgrade pip
              pip install .[dev]
    ```

  - Then, run pytest:

    ```yaml
    ...
      ...
        ...
          - name: Test with pytest
            run: |
              pytest
    ```

  - Finally, to the top of the file, state when you want this workflow to be run. We want to run on every push to main and on every change or creation of pull requests.

    ```yaml
    on:
      push:
        branches:
          - main
      pull_request:
        branches:
          - main
    ```

- Add this section to `pyproject.toml`:

  ```
  [project.optional-dependencies]
  dev = ["pytest"]
  ```

  - Note: This replaces the need for running `pip install pytest` and pytest is installed when we run `pip install .[dev]`

## Commit, push and make a PR

- `git checkout -b add-ci-workflow`
- `git add -p`
- `git add .github/workflows/ci.yaml`
- `git commit -m "Add ci workflow"`
- `git push origin add-ci-workflow`

- In GitHub, make a Pull Request from the `add-ci-workflow` branch to the `main` branch. Wait a bit with accepting the PR.

## Check code formatting

- While there are many freedoms in how you write your Python program, there are also style guides for how to write code consistently. The most renowned is PEP8 (Python Enhancement Proposal #8), written amongst others by the author of Python himself, Guido van Rossum. The authors also give some good reflections on how to relate to the style guide:

> A style guide is about consistency. Consistency with this style guide is important.
> Consistency within a project is more important. Consistency within one module or
> function is the most important.
>
> However, know when to be inconsistent – sometimes style guide recommendations just
> aren’t applicable. When in doubt, use your best judgment. Look at other examples and
> decide what looks best. And don’t hesitate to ask!
>
> In particular: do not break backwards compatibility just to comply with this PEP!
>
> -- <cite>Guido van Rossum et al., [PEP8](https://peps.python.org/pep-0008/) </cite>

- A popular tool for checking that your code is consistent with this guide is Black.

> The coding style used by Black can be viewed as a strict subset of PEP 8.
>
> -- <cite>[The Black code style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)</cite>

- Run `pip install black`
- Run `black --help` to see the help text with an usage guide
- Run `black --check .`
- Run `black --diff .`
- Run `black .` to let Black format all your .py files in the current directory
- Extend the dev requirements in pyproject.toml to be `dev = ["black", "pytest"]`
- Add Black check to the ci.yaml workflow file:

  ```yaml
  ...
    ...
      ...
        - name: Check code formatting
          run: |
            black --check .
  ```

## Commit changes

- `git add -p`
- `git commit -m "Add code formatting check`

## Type hinting and type checking

- Type hints was introduced in Python 3.5 with [PEP484](https://peps.python.org/pep-0484/). The description states: "The proposal is strongly inspired by mypy", which is the tool we will be using to check type hinting.
- "Python is a dynamic language, so usually you’ll only see errors in your code when you attempt to run it. Mypy is a static checker, so it finds bugs in your programs without even running them!" - https://mypy.readthedocs.io/en/stable/

- Run `mypy --help` for help text
- Run `mypy` or `mypy .` to check all your .py files in the current directory
- Extend the dev requirements in pyproject.toml to be `dev = ["black", "mypy", "pytest"]`
- Add a new section in pyproject.toml:

  ```yaml
  [tool.mypy]
  exclude = ["build"]
  files = ["src", "tests"]
  ```

- Add the following to ci.yaml

  ```yaml
  ...
    ...
      ...
        - name: Type checking
          run: |
            mypy
  ```

- Add type hints to the `find_average` function.
  <a title="def find_average(numbers: Sequence[int]) -> float:"> (Hover for hint) </a>

## Commit, push and observe the changes to the PR

- `git add -p`
- `git commit -m "Add type checking`
- `git push origin add-ci-workflow`

## Break the workflow

- Experiment with adding changes that breaks either the tests, the formatting or the static type checking

## Accept the PR

- Restore PR to a working state.
  - You can remove unwanted commits with `git rebase -i origin/main`
- Click the "Rebase and merge" button on GitHub
- Delete the branch on the remote origin (Press the button on GitHub)
- Delete the local branch
  - `git lg` to see the current shape of your history
  - `git fetch origin --prune`
  - `git rebase origin/main`
  - `git checkout origin/main` or (`git checkout main` and `git rebase origin/main`)
  - `git branch -d add-ci-workflow`
