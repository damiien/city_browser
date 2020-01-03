from flask import request, Blueprint, g
from ..models.CountryModel import CountryModel, CountrySchema
from .BaseView import create_response;

country_api = Blueprint('country_api', __name__)
country_schema = CountrySchema()

@country_api.route('/', methods=['GET'])
def get_all():

  countries = CountryModel.get_all()
  result = country_schema.dump(countries, many=True)
  return create_response(result, 200)

@country_api.route('/<country_code>', methods=['GET'])
def get_country(country_code):

  country = CountryModel.get_one(country_code)
  if not country:
    return create_response({'error': 'country not found'}, 404)
  result = country_schema.dump(country)
  return create_response(result, 200)
  
@country_api.route('/continent/<continent>', methods=['GET'])
def get_by_continent(continent):

  countries = CountryModel.get_by_continent(continent)
  result = country_schema.dump(countries, many=True)
  return create_response(result, 200)
