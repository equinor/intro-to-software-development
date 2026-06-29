# Setting up your working environment

## Get the code

- Make a fork of the repository (top-right "Fork" button on GitHub)
- Open Codespaces (green "Code" button → "Codespaces" → "Create codespace")
- (optionally) Authenticate with your account to sync up your settings and extensions
- Change to the `exercises` branch with `git switch exercises`

## Find your way around

- Navigate the filesystem with `pwd`, `ls` and `cd`
- Check the tool versions you have available:
  - `python --version` 
    - Should be 3.13 or newer 
    - If you see the error `python not found` try `python3` instead of `python`
  - `git --version`
- Try interactive python
  - `python` or `ipython`
  - `print("Python is better than C++")`
  - Verify it runs and prints the expected output
  - Exit again with `exit()` or `Ctrl-D`

## Set up a virtual environment

A virtual environment keeps the packages for this project isolated from the rest of
your system.

- Create the virtual environment: `python -m venv .venv`
- Activate it:
  - macOS / Linux: `source .venv/bin/activate`
  - Windows (PowerShell): `.venv\Scripts\Activate.ps1`
  - Windows (CMD): `.venv\Scripts\activate.bat`
- Your prompt line should now start with `(.venv)`
- Verify correct environment is activated:
  - `which python`
    - Should be something like 
      - `/Users/<your_username>/<path_to_project>/intro-to-software-development/.venv/bin/python`
    - Should NOT be anything like 
      - `/opt/homebrew/bin/python3.12`
      - `/Library/Frameworks/Python.framework/Versions/3.11/bin/python3`
      - `C:\Program Files\Python<Version>\`
      - `C:\Users\<YourUsername>\AppData\Local\Programs\Python\Python<Version>\`
  - `pip -V` should also point inside the `.venv` folder
- Upgrade pip so we start from a known-good baseline: `python -m pip install --upgrade pip`
- Tip: deactivate the environment with `deactivate` when you are done

## Tell git who you are

Before your first commit, git needs to know your name and email so your commits are
attributed correctly. In a fresh Codespace this is usually set up for you, but it is
worth checking:

- `git config --global user.name` and `git config --global user.email`
- If either is empty, set them (use the same email as your GitHub account):
  - `git config --global user.name "Your Name"`
  - `git config --global user.email "you@example.com"`