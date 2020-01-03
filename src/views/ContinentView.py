from flask import request, Blueprint, g
from sqlalchemy import text
from ..models import db
from .BaseView import create_response;

continent_api = Blueprint('continent_api', __name__)

@continent_api.route('/', methods=['GET'])
def get_all():

  sql = text('select distinct(country.continent) from country')
  result = db.engine.execute(sql)
  result = [row[0] for row in result]
  return create_response(result, 200)
