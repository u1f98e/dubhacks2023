## Setup
- (Optional) Create a venv to avoid polluting your system packages
  - Run `python3 -m venv .venv`
  - Run `source .venv/bin/activate` to enter the virtual environment
  	- (For Powershell, run `Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force`, then `.venv/bin/activate.ps1`)
  - In VSCode, do `Ctrl+Shift+P`, type "Select Interpreter", and pick the python3.11 inside the .venv folder you created (`.venv/bin/python3.11`)

- In the `backend` folder
  - Run `pip install -r requirements.txt`

- In the `client` folder
  - Run `npm install`
  - Run `npm run build`

## Running
(In the `backend` folder)
Run the flask app using `flask run --debug`

If database updates have happened, run: `python3 run_migration.py`