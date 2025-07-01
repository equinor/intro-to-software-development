# Introduction to Software Development, Git and Python

## Agenda

Day 1

- 09:00 Git & Python, Part 1 (Lars Petter Øren Hauge and Thomas Sundvoll)
  - [Introduction](course_documentation/introduction.md)
  - [Exercise 0: Working Environment](course_documentation/exercises/0_working_environment.md)
  - [Exercise 1: Setup Package Structure](course_documentation/exercises/1_setup_package_structure.md)
- 11:30 Lunch
- 13:00 Git & Python, Part 2 (Lars Petter Øren Hauge and Thomas Sundvoll)
  - [Exercise 2: Writing Your First Test](course_documentation/exercises/2_writing_you_first_test.md)
  - [Exercise 3: Continuous Integration](course_documentation/exercises/3_continuous_integration.md)
  - [Exercise 4: Implement Gardner's Equation](course_documentation/exercises/4_implement_gardners_equation.md)

Day 2

- 09:00 Git & Python, Part 3 (Lars Petter Øren Hauge and Thomas Sundvoll)
  - Recap from yesterday
    - Setup codespaces and virtual environment
    - Python packaging structure
    - Intro to Git
    - Intro to Test Driven Development (TDD) and unit tests with pytest
    - Continuous Integration with GitHub Actions
    - Implementing Gardner's Equation with TDD
  - Intermediate Git: Git merge and git rebase
  - Intermediate GitHub Actions
    - Recap from yesterday
    - Some example from one of our repositories:
      - https://github.com/equinor/isar/tree/main/.github/workflows
  - Intermediate Pytest
    - [Exercise 6: More on unit testing](course_documentation/exercises/6_more_on_unit_testing.md)
  - Refactoring
    - [Exercise 7: More on unit testing](course_documentation/exercises/7_refactor/7_refactor_with_confidence.md)


- 11:30 Lunch
- 13:00 Application Security (Stein-Arne Sivertsen)

Day 3

- 09:00 Data Science, Part 1 (Martin Bjerke and Phillipe Nivlet)
- 11:30 Lunch
- 13:00 Data Science, Part 2 (Martin Bjerke and Phillipe Nivlet)

## Learning goals

### Python and Packaging

- Virtual environments
- The structure of a Python package
- pip install
- Functions and parameters
- Modules and imports
- Context managers
- Testing with pytest, Test Driven Development
- Typehinting, [PEP484](https://peps.python.org/pep-0484/)
- Formatting with Black, [PEP8](https://peps.python.org/pep-0008/)
- Documentation in docstrings, [PEP257](https://peps.python.org/pep-0257/)
- (optional) Classes and dataclasses
- (optional) Error handling (try / catch)
- (optional) Dunder methods and attributes (`__file__`, `__init__()`)
- (optional) Pytest fixtures and parameterize
- (optional) Decorators

### Git and GitHub

- Git Commands
  - git status, git diff
  - git add -p, git commit, git push
  - git checkout
  - git pull (git fetch, git rebase)
  - git log, git log --oneline
  - git remote -v
  - git fetch, git rebase
  - (optional) git commit --amend, git commit --fixup, git rebase -i --autosquash
  - (optional) git cherry-pick
- Branches, Remotes, Pull Requests
- The review process
- Branch protection rules (optional)
- Continuous Integration with GitHub Actions

### Application Security

- Threat landscape & AppSec
- Snyk
- LLM Hacking

### Data Science

- Numpy
- Working with csv files
- numpy, pandas, dataframes
- visualization and plotting
- machine learning, support vector machines, classification, regression

## Useful links

A couple of useful links are provided [here](course_documentation/useful_links.md).
