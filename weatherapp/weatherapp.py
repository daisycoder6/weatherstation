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



@route('/new', method='GET')
def new_item():

    new = request.GET.task.strip()

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()

    c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

@route('/todo')
def todo_list():
    conn = sqlite3.connect('temps.db')
    c = conn.cursor()
    c.execute("SELECT id, temp FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    return str(result)



if __name__ == '__main__':

    run(host='localhost', port=8080,debug=True,reload=True)