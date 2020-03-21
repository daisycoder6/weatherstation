from bottle import Bottle, run, get, post,static_file
from bottle import request, route, template, response
import time
import random
import sqlite3




@route('/')
def display_weather():

    airtemp = request.query.field1
    airhumid = request.query.field2

    conn = sqlite3.connect('temps.db')
    c = conn.cursor()

    c.execute("INSERT INTO meas (temp,humid) VALUES (?,?)", (airtemp, airhumid))
    new_id = c.lastrowid

    conn.commit()
    
    #airtemp = str(random.random())

    #return "Hello World" + airtemp
    # return template('Temperaturedjfbv: {{airtemp}} Humidity {{airhumid}}', 
    #                 airtemp=airtemp, airhumid=airhumid)

    return '<p>The new task was inserted into the database, the ID is %s</p>' % airtemp




@route('/table')
def todo_list():
    conn = sqlite3.connect('temps.db')
    c = conn.cursor()
    c.execute("SELECT id, temp, humid FROM meas ORDER BY id DESC LIMIT 10")
    result = c.fetchall()
    return template('make_table', rows = result)

# SELECT * FROM (
# SELECT * FROM employees ORDER BY employee_id DESC LIMIT 10)
# ORDER BY employee_id ASC;


if __name__ == '__main__':

    run(host='localhost', port=8080,debug=True,reload=True)