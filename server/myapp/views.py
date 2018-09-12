
from datetime import datetime
from decimal import Decimal
import logging
import os

from flask import abort
from flask import jsonify
from flask import render_template
from flask import request
from flask import Response
# from flask_httpauth import HTTPBasicAuth
from werkzeug.contrib.cache import SimpleCache

from myapp import app
from galiboo import Galiboo

from myapp.services import get_hello_world
from myapp.youtube_services import youtube_search
from myapp import galiboo_services

logger = logging.getLogger(__name__)
cache = SimpleCache()
# galiboo_client = Galiboo(env['GALIBOO_KEY'])

# auth = HTTPBasicAuth()
# cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# users = {
#     "admin": "admin"
# }
galiboo_client = Galiboo(os.getenv("GALIBOO_KEY"))


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

@app.route('/api/v1/search_youtube', methods=['GET'])
def search_youtube():
    if request.method == 'GET':
        q = request.args.get('q', '')
        return jsonify(youtube_search(q))
    else:
        raise InvalidUsage('Only GET is allowed', status_code=400)

@app.route('/api/v1/search_galiboo_smart_search', methods=['GET'])
def search_galiboo_smart_search():
    if request.method == 'GET':
        q = request.args.get('q', '')
        q = q.replace('+', ', ')
        return jsonify(galiboo_services.smart_search(galiboo_client, q))
    else:
        raise InvalidUsage('Only GET is allowed', status_code=400)

@app.route('/api/v1/search_galiboo_tracks', methods=['GET'])
def search_galiboo_tracks_search():
    if request.method == 'GET':
        q = request.args.get('q', '')
        q = q.replace('+', ', ')
        return jsonify(galiboo_services.tracks_search(galiboo_client, q))
    else:
        raise InvalidUsage('Only GET is allowed', status_code=400)

@app.route('/api/v1/search_galiboo_tracks_by_artist', methods=['GET'])
def search_galiboo_tracks_by_artist_search():
    if request.method == 'GET':
        q = request.args.get('q', '')
        q = q.replace('+', ', ')
        return jsonify(galiboo_services.tracks_by_artist_search(galiboo_client, q))
    else:
        raise InvalidUsage('Only GET is allowed', status_code=400)

@app.route('/api/v1/search_galiboo_similiar', methods=['GET'])
def search_galiboo_similiar():
    if request.method == 'GET':
        track_id = request.args.get('track_id', '')
        return jsonify(galiboo_services.similiar_search(galiboo_client, track_id))
    else:
        raise InvalidUsage('Only GET is allowed', status_code=400)

