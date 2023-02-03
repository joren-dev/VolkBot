# VolkBot
A discord bot for educational purposes, a collective project from HHS students.

## Prerequisites
1. Install [Python 3.11.0](https://www.python.org/downloads/). During installation make sure to:
	- Include [Python PIP](https://pip.pypa.io/en/stable/installation/) in installation
	- Mark the 'Add python.exe to PATH' checkbox.

2. Open operation system's terminal and run the following commands to double-check if all requirements are available:
    - `python --version` -> possible output: `Python 3.11.0`
    - `python -m pip --version` -> possible output: `pip 22.3.1`

3. Install [Pipenv](https://github.com/pypa/pipenv#installation) by running command: `pip install --user pipenv`

4. Check if it installed by running the following command:
    - `python -m pipenv --version` -> possible output: `pipenv, version 2022.11.25`


## Setup project for official collaborators?
1. Download or clone the main branch to a local folder named `volk_bot` by doing: `git clone https://github.com/joren-dev/VolkBot.git`
2. Open terminal inside project.
3. Create local pipenv: `pipenv install`.
4. Activate it with: `pipenv shell` after getting the dependencies.
5. Open folder inside Visual Code and press "Select interpreter".
6. On windows navigate to: `C:\Users\xxxx\.virtualenvs\` and find the `volk_bot-xxxxxxxx` folder.
7. Select the `volk_bot\Scripts\python.exe` as interpreter.
 
## How to fork the project for contributor?
1. Press fork on the top right of the screen
2. Create a forked repository of VolkBot
3. Follow the steps from official collaborators, but clone the forked repository instead.
4. Create a branch for your feature, using: `git checkout -b feature_name`
5. Start writing code in that branch

## How to Pull Request my code?
_coming soon_

 ## Common dev-commands explained
 This codebase has various commands a developer might want to use when contributing to this project. All the
 commands start off with `pipenv run` to ensure you're working inside the assigned virtual environment.


- `pipenv run pip --version`
This is how you use pip inside pipenv, dont forget the `run`.

- `pipenv run black "../volk_bot"`
Same goes for black formatter, ensure you are inside the "\volk_bot\" directory or adapt the relative path accordingly

## Environment file
The .env file contains parameters for the local install that will not be committed like the discord API token or channel ids. You can take a look at [[file:.env.example]].
```
TOKEN=ADDYOURTOKENHERE
```