# Introduction to Software Development, Git and Python

## Content

In this course, we will set up a simple Python package. It will concern some simple
calculations within the geology domain, so we will name it `geo-calculator`.

Along the way, you will get familiar with the packaging structure of Python and how a
modern Python package typically looks.

We will also embed git into our workflow, learn / refresh the basic git commands, and
possibly touch upon some more advanced commands.

Quite early we will write some unit tests, which verify intended functionality.

We will set up a workflow in GitHub Actions for doing continuous integration with your
remote repository, including running your tests and static code analysis.

Towards the end of this section we will use what we have learned to implement the
calculation of a specified geological property.

The main learning goal is to be familiar with the development process, and learn some
software craftsmanship along the way.

## Agenda

Day 1

- 09:00 Git & Python, Part 1
  - Introduction
    - Round around the table
      - Name
      - Where and what you study
      - Internship location (Trondheim, Bergen, Stavanger, Oslo?)
      - Short about the project
      - Optionally what you hope to learn in the course
- 11:30 -- Lunch --
- 13:00 Git & Python, Part 2

Day 2

- 09:00 Git & Python, Part 3
- 11:30 -- Lunch --
- 13:00 Application Security

Day 3

- 09:00 Data Science, Part 1
- 11:30 -- Lunch --
- 13:00 Data Science, Part 2

## Learning goals

Python and Packaging

- Virtual environments
- Package structure in Python
- pip install
- Functions and parameters
- Documentation in docstrings (https://peps.python.org/pep-0257/)
- Typehinting
- Modules and imports
- Testing with pytest
- Linting with Black
- Dunder methods and attributes (`__file__`, `__init__()`)

Git and GitHub

- git add, git commit, git push
- git checkout
- git pull (git fetch, git rebase)
- git log, git log --oneline
- branches, remotes, pull requests
- review process
- branch protection rules (optional)
- Continuous Integration with GitHub Actions

Tooling

- Codespaces on GitHub
- Configuring VS Code

Cyber Security

Data Science

- Numpy
- Working with csv files
- numpy, pandas, dataframes
- visualization and plotting
- machine learning, support vector machines, classification, regression

Bonus

- Experiment with typehinting and mypy (add this to the GitHub)
- rebasing, cherry-picking, amending, fixup, autosquash
- Classes and dataclasses
- Context managers
- Decorators (pytest)
- Error handling (try / catch)
- Input sanitaion (velocity < 0 for gardners equation)
- Auto-formatting in VS Code (linelength 88)

## Ideas for further exercises

- Set up your own new github repository
  - Configure Pull Request (Allow rebase merging)
  - Add branch protection to require PR

## Course outline

1. Setup package structure
   - Create files
   - Commit work to local
   - Push to remote
2. Writing your first test
   - TDD; make failing test, then let it pass
   - implement find_average
   - Present some benefits of writing good tests (in advance). E.g. change code with confidence later
3. Continuous integration
   - Add workflow
   - Add formating
   - Add typehinting
   - Create Pull Request (make this mandatory on your fork)
4. Implement gardners equation
   - Receive a finished test for gardners equation
   - Bonus: Play around with Pytest approx. Find out from docs what the default tolerance is
   - Receive a finished test (skipped) for inverse gardners equation
   - Bonus: Add requirement to handle negative velocity (new test, skipped initially)
