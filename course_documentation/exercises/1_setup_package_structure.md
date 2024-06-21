# Exercise 1: Setup package structure

- Choose a name for your package: "geo-calculator"
- Create a /src file
- Create a project file /src/package name
- Add `__init__.py` file to /src/geo_calculator/

## Set up a virtual environment

- Run `python -m venv venv` to create the virtual environment
- Run `source venv/bin/activate` to activate the virtual environment

## Install your package

- Run `pip install -e .[dev]`
  <a title="My secret hint"> Hover for hint </a>

## Versioning

- Add the following to the `__init__.py` file to /src/geo_calculator/

```python
from importlib.metadata import version

__version__ = version(__package__ or __name__)
```

- `pip install -e .`
- Open interactive python
- `import geo_calculator`
- Verify that `geo_calculator.__version__` outputs a version

## Add missing pieces

- `pyproject.toml`
  - Skip pytest and the optional stuff (show a minimal file to start with)
- LICENSE
- README.md
- .gitignore
