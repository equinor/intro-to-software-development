# Exercise 1: Setup package structure

- Choose a name for your package: "geo-calculator"
- Create a /src file
- Create a project folder /src/geo_calculator/
- Add `__init__.py` file to /src/geo_calculator/

## Set up a virtual environment

- Run `python -m venv venv` to create the virtual environment
- Run `source venv/bin/activate` to activate the virtual environment

## Install your package

- Run `pip install -e .`
  <a title="My secret hint"> Hover for hint </a>

## Add missing pieces

- `pyproject.toml`. NB `name = "geo-calculator"` with hyphen, not underscore.
  - Skip pytest and the optional stuff (show a minimal file to start with)
- LICENSE
- README.md
- .gitignore

## Import package

- Open interactive python

```python
import geo_calculator
geo_calculator.__file__
```

## git commit

- Introduction (Lars Petter)

  - Version control
  - Distributed
  - Snapshots
  - What are the hashes and tags
  - Commit messages
  - git status
  - git log
  - git add
  - git commit
  -

- Commit your work;
- "Add pyproject.toml"
- "Add LICENSE"
- "Add README.md"
- "Add .gitignore"
- "Add src folder" (everything withing src)
