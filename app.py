from flask import Flask
from blueprints.index import index_views
from blueprints.claims import claim_views

import os

app = Flask(__name__)

# config
app.config.from_object('config')
if os.path.exists('config/local_settings.py'):
    app.config.from_object('config.local_settings')

# blueprints
app.register_blueprint(index_views)