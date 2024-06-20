# Course Agenda

## Warm up quiz

## First exercise: Setup package strucutre

- Choose a name for your package: "geo-calculator"
- Create a /src file
- Create a project file /src/package name
- Add `__init__.py` file to /src/geo_calculator/

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

## Implement Gardner's equation: https://en.wikipedia.org/wiki/Gardner%27s_relation
