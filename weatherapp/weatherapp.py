from bottle import Bottle, run, get, post,static_file
from bottle import request, route, template, response
import datetime
import random
import sqlite3

dbasename = 'temps2.db'

def gen_tstamp():
    """
    Generates a current timestamp
    """
    i = datetime.datetime.now()
    tstamp = i.strftime('%Y_%m_%d_%H_%M_%S')

    return tstamp


@route('/')
def display_weather():



    sensorid = request.query.sensorid
    tstamp = gen_tstamp()
    airtemp = request.query.field1
    airhumid = request.query.field2

    conn = sqlite3.connect(dbasename)
    c = conn.cursor()

    c.execute("INSERT INTO meas (sensor_id , tstamp, temp, humid) VALUES (?,?,?,?)", 
                                (sensorid, tstamp, airtemp, airhumid))
    new_id = c.lastrowid

    conn.commit()
    
    #airtemp = str(random.random())

    #return "Hello World" + airtemp
    # return template('Temperaturedjfbv: {{airtemp}} Humidity {{airhumid}}', 
    #                 airtemp=airtemp, airhumid=airhumid)

    return '<p>The new task was inserted into the database, the ID is %s</p>' % airtemp




@route('/table')
def todo_list():
    conn = sqlite3.connect(dbasename)
    c = conn.cursor()
    c.execute("SELECT id, sensor_id, tstamp, temp, humid FROM meas ORDER BY id DESC LIMIT 10")
    result = c.fetchall()

    return template('make_table', rows = result)



if __name__ == '__main__':

    run(host='localhost', port=8080,debug=True,reload=True)