## Setup
- (Optional) Create a venv to avoid polluting your system packages
  - Run `python3 -m venv .venv`
  - Run `source .venv/bin/activate` to enter the virtual environment
  - In VSCode, do `Ctrl+Shift+P`, type "Select Interpreter", and pick the python3.11 inside the .venv folder you created (`.venv/bin/python3.11`)

- Run `pip install -r requirements.txt`

## Running

Run the flask app using `flask --app server run`
or `python3 -m flask --app server run`