from pathlib import Path

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path, verbose=True)
load_dotenv(verbose=True)

app = Flask(__name__)
CORS(app)
app.logger.info('app setup finished')

from myapp import views

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
