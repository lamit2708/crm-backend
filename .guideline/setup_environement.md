# Guideline to setup environment

## Create virtual environment

python3 -m venv env

## Use this environment

source ./env/bin/activate

## Export the python library package

pip freeze > requirements.txt

## Install environment from requirements

pip install -r requirements.txt
