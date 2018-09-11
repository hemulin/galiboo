
from datetime import datetime
from decimal import Decimal
import logging

from flask import abort
from flask import jsonify
from flask import render_template
from flask import request
from flask import Response
from flask_dotenv import DotEnv
# from flask_httpauth import HTTPBasicAuth
from werkzeug.contrib.cache import SimpleCache

from myapp import app
# from galiboo import Galiboo

from myapp.services import get_hello_world

logger = logging.getLogger(__name__)
cache = SimpleCache()
env = DotEnv(app)
# galiboo_client = Galiboo(env['GALIBOO_KEY'])

# auth = HTTPBasicAuth()
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# users = {
#     "admin": "admin"
# }


# @auth.get_password
# def get_pw(username):
#     if username in users:
#         return users.get(username)
#     return None

#####################
####### Routes ########
#####################

@app.route('/api/v1/hello', methods=['GET'])
def hello_world():
    if request.method == 'GET':
        # print(galiboo_client)
        return 'Hello, World!'
    else:
        raise InvalidUsage('Only GET is allowed', status_code=400)

@app.route('/api/v1/hello2', methods=['GET'])
def hello_world2():
    if request.method == 'GET':
        return jsonify(get_hello_world())
    else:
        raise InvalidUsage('Only GET is allowed', status_code=400)
