from __future__ import unicode_literals
from __future__ import absolute_import
from bottle import Bottle, redirect, run

from switchboard import operator, configure
from switchboard.middleware import SwitchboardMiddleware
from switchboard.admin import app as switchboard

configure({'mongo_timeout': 1000})

app = Bottle()
app.mount('/_switchboard/', switchboard)


@app.get('/')
def index():
    if operator.is_active('example'):
        return 'The example switch is active.'
    else:
        return 'The example switch is NOT active.'


@app.get('/_switchboard')
def trailing_slash():
    redirect('/_switchboard/')


app = SwitchboardMiddleware(app)


run(app, host='localhost', port=4588, debug=True,
    reloader=False)
