from flask import Flask, session
from datetime import timedelta
from flask_cors import CORS
from flask_caching import Cache
from settings import CORS_RESOURCES, CACHE_CONFIG
import hashlib


app = Flask(__name__, template_folder='templates')
app.secret_key = 'ws-project'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=15)



CORS(app=app, resources=CORS_RESOURCES)




cache = Cache(config=CACHE_CONFIG)
cache.init_app(app=app)
