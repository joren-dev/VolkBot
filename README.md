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


## How to contribute to this project
Please refer to [this](https://github.com/joren-dev/VolkBot/blob/main/.github/CONTRIBUTING.md) link for a detailed step-by-step explanation on how to contribute to this public repostory. Do
know that in the future there will be video tutorials linked to make it even easier to get started.


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