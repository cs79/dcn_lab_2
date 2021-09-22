from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/time')
def the_time_is_now():
    return 'The time is {}'.format(datetime.strftime(datetime.now(), "%H:%M:%S"))

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
