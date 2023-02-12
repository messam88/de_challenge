#!/usr/bin/env python

import csv
import json
import sqlalchemy
import logging

engine = sqlalchemy.create_engine("mysql://codetest:swordfish@database/codetest")

with engine.connect() as con:
    try:
        with open("schema.sql") as file:
            query = sqlalchemy.text(file.read())
            con.execute(query)
    except IOError:
        logging.exception('Failed to load schema.sql')