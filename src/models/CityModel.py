from marshmallow import fields, Schema
from . import db

class CityModel(db.Model):

  __tablename__ = 'city'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  countrycode = db.Column(db.String(3), unique=True, nullable=False)
  district = db.Column(db.String(128), nullable=False)
  population = db.Column(db.String(128))

  def __init__(self, data):
    self.id = data.get('id')
    self.name = data.get('name')
    self.countrycode = data.get('countrycode')
    self.district = data.get('district')
    self.population = data.get('population')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def update(self, data):
    for key, item in data.items():
      setattr(self, key, item)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @staticmethod
  def get_all():
    return CityModel.query.all()

  @staticmethod
  def get_one(id):
    return CityModel.query.get(id)
  
  @staticmethod
  def get_by_country_code(value):
    return CityModel.query.filter_by(countrycode=value).all()

  def __repr(self):
    return '<id {}>'.format(self.id)

class CitySchema(Schema):
  id = fields.Int(dump_only=True)
  name = fields.Str(required=True)
  countrycode = fields.Str(required=True)
  district = fields.Str(required=True)
  population = fields.Int(dump_only=True)
