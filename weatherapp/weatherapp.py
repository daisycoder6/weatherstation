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
def gather_sensor_data():
    """
    Sensors send data here using Querystrings.
    Gets stored in sqlite database
    """

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

    return 




@route('/table')
def display_data():
    """
    Displays last ten results in a table
    """

    conn = sqlite3.connect(dbasename)
    c = conn.cursor()
    c.execute("SELECT id, sensor_id, tstamp, temp, humid FROM meas ORDER BY id DESC LIMIT 10")
    result = c.fetchall()

    output = template('topten2', rows=result)

    return output



@route('/static/<filename:path>')
def fetch_static(filename):
    """
    Serves upthe static content. we require the path filter
    as wehave subdirectories under static
    """
    #response.set_header('Cache-Control', 'max-age=600')
    return static_file(filename, root='static')


if __name__ == '__main__':

    run(host='localhost', port=8080,debug=False,reload=False)