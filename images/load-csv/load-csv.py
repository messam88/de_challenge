#!/usr/bin/env python

import csv
import json
import sqlalchemy
import logging

# maping places with their ids as cache
place_maping = {}

# connect to the database
engine = sqlalchemy.create_engine(
    "mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

# load places.csv
place = sqlalchemy.schema.Table(
    'place', metadata, autoload=True, autoload_with=engine)

try:
    with open('/data/places.csv') as places_csv_file:
        reader = csv.reader(places_csv_file)
        next(reader)
        for row in reader:
            query = sqlalchemy.insert(place).values(
                city=row[0], county=row[1], country=row[2])
            result = connection.execute(query)
            place_maping[row[0]] = result.inserted_primary_key[0]
except IOError:
    logging.exception('Failed to load places.csv')


# load people.csv
person = sqlalchemy.schema.Table(
    'person', metadata, autoload=True, autoload_with=engine)

try:
    with open('/data/people.csv') as people_csv_file:
        reader = csv.reader(people_csv_file)
        next(reader)
        for row in reader:
            query = person.insert().values(place_id=place_maping.get(row[3]), given_name=row[0], family_name=row[1], date_of_birth=row[2])
            connection.execute(query)
except IOError:
    logging.exception('Failed to load people.csv')