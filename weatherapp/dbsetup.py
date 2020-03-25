"""
Inital setupof database

Usage: python dbsetup.py <databasename>

Run from app directory
"""


import argparse
import sqlite3


parser = argparse.ArgumentParser()
parser.add_argument("database_name", default = 'results.db', help ="Database Name")

args=parser.parse_args()


conn = sqlite3.connect(args.database_name) # Warning: This file is created in the current directory
conn.execute("CREATE TABLE meas (id INTEGER PRIMARY KEY, sensor_id char(3) NOT NULL, tstamp char(22) NOT NULL, temp char(5) NOT NULL, humid char(5) NOT NULL)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Read A-byte-of-python to get a good introduction into Python',0)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Visit the Python website',1)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Test various editors for and check the syntax highlighting',1)")
# conn.execute("INSERT INTO todo (task,status) VALUES ('Choose your favorite WSGI-Framework',0)")
conn.commit()