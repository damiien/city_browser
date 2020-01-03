from flask import request, Blueprint, g
from ..models.CityModel import CityModel, CitySchema
from .BaseView import create_response;

city_api = Blueprint('city_api', __name__)
city_schema = CitySchema()

@city_api.route('/', methods=['GET'])
def get_all():

  cities = CityModel.get_all()
  result = city_schema.dump(cities, many=True)
  return create_response(result, 200)
  
@city_api.route('/country/<country_code>', methods=['GET'])
def get_by_country_code(country_code):

  cities = CityModel.get_by_country_code(country_code)
  result = city_schema.dump(cities, many=True)
  return create_response(result, 200)

@city_api.route('/<city_id>', methods=['GET'])
def get_city(city_id):

  city = CityModel.get_one(city_id)
  if not city:
    return create_response({'error': 'city not found'}, 404)
  result = city_schema.dump(city)
  return create_response(result, 200)

@city_api.route('/<city_id>', methods=['PUT'])
def update(city_id):

  req_data = request.get_json()
  data, error = city_schema.load(req_data, partial=True)
  if error:
    return create_response(error, 400)

  city = CityModel.get_one(city_id)
  city.update(data)
  result = city_schema.dump(city)
  return create_response(result, 200)

@city_api.route('/<city_id>', methods=['DELETE'])
def delete(city_id):

  city = CityModel.get_one(city_id)
  city.delete()
  return create_response({'message': 'deleted'}, 204)
  