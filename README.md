# Readme for carpark_romania
- public_data_hacking/carpark_romania.py

## Install virtualenv
	sudo apt-get install virtualenv

## Set up dev environment
	virtualenv -p python3.6 venv
- create new isolated environment with python3 as the interpreter

## Activate it
	source venv/bin/activate

## Install third party libraries
	pip install -r requirements.txt
- just the requests module for now

## Run script
	python carpark_romania.py

## Deactivate virtual env
	deactivate
