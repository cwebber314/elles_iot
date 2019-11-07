"""
Flask server which handles GET from the IoT 
"""
from flask import Flask, request
import datetime as dt
import pdb
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/heartbeat')
def heartbeat():
    return 'I am alive'

@app.route('/position')
def position():
    """
    get position data from sensor.  The data is embedded in the URL parameters, you can test it like this
    `http://localhost:8001/position?position=1&comment=foo`
    """
    position = request.values.get('position', -1)
    comment = request.values.get('comment', 'no comment')

    # do whatever you want with the data now.
    # write it to a db, to a file, etc
    s = 'payload: {}, {}'.format(position, comment)
    print(s) 

    with open('_position.txt', 'a') as f:
        f.write("{}, {}, {}".format(dt.datetime.now(), position, comment))
        f.write("\n")

    return s

    
app.run(host='0.0.0.0', port=8001, debug=True)