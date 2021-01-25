# Advent Of Code 2020

This year I decided to brush up my Python skills.

The project uses poetry as a package manager and pyenv as a python version manager

## Usage
### Initialize a local environment with pyenv
`pyenv local 3.8`

### Install venv and dependencies
`poetry install`

### Run the daily challenges
`poetry run day<number> ./data/day<number>/input.txt`
or using the test input
`poetry run day<number> ./data/day<number>/test_input.txt`

### Run the tests
`poetry run pytest --cov`

### lint
`poetry run flake8 src tests`