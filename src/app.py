from flask import Flask, render_template

from .config import app_config
from .models import db

from .views.CountryView import country_api
from .views.CityView import city_api
from .views.ContinentView import continent_api

def create_app(env_name):

	app = Flask(__name__, static_folder = './public', template_folder="./static")
	app.config.from_object(app_config[env_name])

	db.init_app(app)

	app.register_blueprint(country_api, url_prefix='/api/countries')
	app.register_blueprint(city_api, url_prefix='/api/cities')
	app.register_blueprint(continent_api, url_prefix='/api/continents')
	
	@app.route('/', methods=['GET'])
	def index():
		return render_template('index.html');
		
	return app