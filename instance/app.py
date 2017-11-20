# instance/app.py

from flask import Flask

# local import
from instance.config import app_config
from instance.db import db, init_testdb
from api.endpoints import api_bp

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(api_bp)

    with app.app_context():
    	db.drop_all()
    	db.create_all()

    	if config_name=='testing':
    		init_testdb()
    
    return app