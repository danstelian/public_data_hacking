# Readme for carpark_romania
- public_data_hacking/carpark_romania.py

## Module doc
	Total number of registered automobiles in Romania in 2017
	(parcauto2017.csv)
	1. Top 5 counties by number of registered cars
	2. Top 5 car brands in a user defined county
	(also the percentages in ralation to the whole country)

	Mostly an excuse to play with Python's list comprehensions,
	Counters, default(dict) and csv files

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
