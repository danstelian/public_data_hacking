"""
Public Data Hacking
Total number of registered automobiles in Romania in 2017
1. Top 5 counties by number of registered cars
2. Top 5 car brands in a user defined county,
and also the percentage compared to the whole country.
3. A lot of possibilities...

Mostly an excuse to play with Python's list comprehensions,
Counters, default(dict) and csv files.
"""


import requests
import csv
import os
from collections import Counter, defaultdict


def read_url(file_name, url):
    # download the file
    r = requests.get(url)
    csv_file = open(file_name, 'wb')
    csv_file.write(r.content)
    csv_file.close()


def read_file(file_name):
    # read the file and return it as a list (of OrderedDict type objects)
    with open(file_name, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        reader.fieldnames[0] = 'JUDET'  # fixing some weird reading mistake

        cars = list(reader)
        # print(reader.fieldnames)
    return cars


def top_counties(cars):
    # top 5 counties by number of cars
    print('Number of cars in 2017 by county:\n#################################')
    counties = Counter()
    for row in cars:
        counties[row['JUDET']] += int(row['TOTAL_VEHICULE'])

    for name, count in counties.most_common(5):
        print(f'{name}: {count}')
    print()


def county_and_brand(cars, county):
    # top 5 car brands in a user defined county
    by_brand = defaultdict(Counter)
    for row in cars:
        by_brand[row['JUDET']][row['MARCA']] += int(row['TOTAL_VEHICULE'])

    # as a point of reference
    total = Counter()
    for row in cars:
        total[row['MARCA']] += int(row['TOTAL_VEHICULE'])

    print('Top 5 car brands in {0} county:\n{1}'.format(county, '#'.rjust(34, '#')))
    for brand, count in by_brand[county].most_common(5):
        # percentage, a certain brand (in the specified county) compared to the same brand in the whole country
        percentage = (int(by_brand[county][brand])/int(total[brand]))*100
        print(f'{brand}: {count}, {percentage:.2f}%')
    print()


def main():
    url = 'http://data.gov.ro/dataset/b93e0946-2592-4ed7-a520-e07cba6acd07/resource/' \
          '4f434c30-0afe-4101-bacd-58b4d95a998e/download/parcauto2017.csv'
    file_name = 'parcauto2017.csv'

    # if the file does not exist
    if not os.path.isfile(file_name):
        read_url(file_name, url)
    # read from the file into a list, not efficient but that is not the point of this exercise
    auto = read_file(file_name)  # cars, trucks, motorcycles, etc.

    # only cars
    cars = [row for row in auto if row['CATEGORIE_NATIONALA'] == 'AUTOTURISM']

    # top 5 counties by number of cars
    top_counties(cars)

    # top 5 car brands in Brasov county
    county_and_brand(cars, 'BRASOV')


if __name__ == '__main__':
    main()