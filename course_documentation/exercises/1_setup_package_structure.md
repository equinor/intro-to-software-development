# Exercise 1: Setup package structure

## Create structure for the geo-calculator package

> **Why a `src/` folder?** Putting your package under `src/` (the "src layout") means the
> package is only importable once it has been installed. This prevents a common class of
> bugs where Python accidentally imports the local source folder instead of the installed
> package, which can hide packaging mistakes until they reach someone else's machine.

- Create a /src folder with from command line or in VS Code
  - `mkdir src`
- Create a project folder /src/geo_calculator/
  - `cd src`
  - `mkdir geo_calculator`
- Add `__init__.py` file to /src/geo_calculator/. This makes it a module.
  - `cd geo_calculator`
  - `touch __init__.py`

## Try to install your package

- Navigate back to the top level with `cd ../..` (or `cd ..` twice)
- Run `pip install -e .`
  - Note: -e means "editable mode" and lets you make modifications to your code and run
    it without having to install the package again.
  - This will fail for now because we are missing some metadata. That's expected — we add it next.

## Add missing pieces

- Create a `pyproject.toml` file at top level and paste the following. First, tooling to build our package:

  ```toml
  [build-system]
  requires = ["setuptools>=64.0", "setuptools_scm>=8"]
  build-backend = "setuptools.build_meta"
  ```

  Then, project / package metadata:

  ```toml
  [project]
  name = "geo-calculator"
  authors = [{ name = "<Your name here>" }]
  description = "Introduction to Software Development course and demo Python package"
  readme = "README.md"
  requires-python = ">=3.13"
  license = { file = "LICENSE" }
  dependencies = ["numpy"]
  dynamic = ["version"]

  [project.urls]
  repository = "https://github.com/<your_github_username>/intro-to-software-development"
  ```

  - Change [project].authors to have your name
  - Change [project.urls].repository to have your github username
  - Note: `name = "geo-calculator"` with hyphen, not underscore.

- Create a `LICENSE` file at top level and paste the following:

  ```
  MIT License

  Copyright (c) 2026 <Your name here>

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
  ```

  - Change the second (third) line to contain your name

- Create a `README` file at top level write a description, for example:

  ```
  # Geo Calculator

  This package provides a simple module for performing geological calculations.
  ```

- Try installing again

## Importing the package

- Open interactive python with `python` or `ipython`
- Run `import geo_calculator`
- Run `geo_calculator.__file__`
- Notice that the path points into your `src/geo_calculator/` folder, confirming the
  editable install works. Exit with `exit()`.
- Back in the terminal, inspect the install:
  - `pip list` should now list `geo-calculator` (with a version and a path for editable installs)
  - `pip show geo-calculator` shows the metadata you wrote in `pyproject.toml`

## git commit

Now is a good time to save the state we are in. We will do this with git. Lars Petter will give an introduction to git.

- If missing, add `.gitignore` file at top level and paste the following:

  ```
  # macOS specific files
  .DS_Store
  .AppleDouble
  .LSOverride
  Icon?
  ._*
  .Spotlight-V100
  .Trashes

  # Python cache & compiled files
  __pycache__/
  *.pyc
  *.pyo
  *.pyd
  *.so

  # Environments & Dependencies
  .venv/
  venv/
  env/
  ENV/
  env.bak/
  venv.bak/
  .env

  # Distribution / Packaging
  build/
  develop-eggs/
  dist/
  downloads/
  eggs/
  .eggs/
  lib/
  lib64/
  parts/
  sdist/
  var/
  wheels/
  *.egg-info/
  .installed.cfg
  *.egg
  MANIFEST

  # IDEs & Editors
  .vscode/*
  !.vscode/settings.json
  !.vscode/launch.json
  .idea/
  *.swp
  *.swo
  ```

- Commit your work so far

  - `git status`: Verify that you are on your main branch
  - Sanity check: `git status` should NOT list `.venv/` or `*.egg-info/`. If it does, your `.gitignore` is not taking effect yet — double-check its contents and location (top level).
  - `git diff`: (Optional) Scroll through to recognize your changes
  - `git add src/geo_calculator/__init__.py`
  - `git add pyproject.toml`
  - `git add LICENSE`
  - `git add README.md`
  - `git add .gitignore`
  - `git diff --staged`: To see which changes you have added (to the staging area)
  - `git commit -m "Setup package structure"`

- Note: Good article on writing good commit messages: https://cbea.ms/git-commit/
