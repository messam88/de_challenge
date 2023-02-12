#!/usr/bin/env python

import csv
import json
import sqlalchemy
import logging

# connect to the database
engine = sqlalchemy.create_engine(
    "mysql://codetest:swordfish@database/codetest")
connection = engine.connect()

metadata = sqlalchemy.schema.MetaData(engine)

person = sqlalchemy.schema.Table(
    'person', metadata, autoload=True, autoload_with=engine)
place = sqlalchemy.schema.Table(
    'place', metadata, autoload=True, autoload_with=engine)

try: 
  with open('/data/summary_ourput.json', 'w') as json_file:
      query = sqlalchemy.select([
        place.columns.country, sqlalchemy.func.count(person.columns.id)
        ]).group_by(place.columns.country)
      rows = connection.execute(query).fetchall()

      rows_dic = {}
      for row in rows:
        # row[0] = country, row[1] = peaople count
        rows_dic[row[0]] = row[1]
      json.dump(rows_dic, json_file, separators=(',', ':'))
except IOError:
  logging.exception('Failed to open summary_ourput.json')