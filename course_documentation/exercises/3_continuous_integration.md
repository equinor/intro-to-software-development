# Setting up continuous integration with GitHub Actions

## Create workflow

- Create ./github/workflows/ci.yaml

```yaml
jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"
```

```yaml
jobs:
  build:
   ...
   steps:
   ...
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install .[dev]
```

```yaml
jobs:
  build:
   ...
   steps:
   ...
      - name: Test with pytest
        run: |
          pytest
```

- Edit `pyproject.toml`. Note: This replaces the need for running `pip install pytest`

```
[project.optional-dependencies]
dev = ["pytest"]
```

## Run formatting

- Run `black --help` to see the help text with an usage guide
- Run `black --check .`
- Run `black --diff .`
- Run `black .` to let Black format all your .py files in the current directory

## Run typehinting

- Run `mypy --help` for help text
- Run `mypy` or `mypy .` to check all your .py files in the current directory

## Make a PR and see that the formatting and typehinting fails
