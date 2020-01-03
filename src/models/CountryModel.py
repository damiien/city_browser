from marshmallow import fields, Schema
import datetime
from . import db

class CountryModel(db.Model):

  __tablename__ = 'country'
  code = db.Column(db.String(3), primary_key=True)
  name = db.Column(db.String(128), nullable=False)
  continent = db.Column(db.String(128), unique=True, nullable=False)
  region = db.Column(db.String(128), nullable=False)
  population = db.Column(db.String(128))

  def __init__(self, data):
    self.name = data.get('name')
    self.continent = data.get('continent')
    self.region = data.get('region')
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
    return CountryModel.query.all()

  @staticmethod
  def get_one(id):
    return CountryModel.query.get(id)
  
  @staticmethod
  def get_by_continent(value):
    return CountryModel.query.filter_by(continent=value).all()

class CountrySchema(Schema):
  code = fields.Str(required=True)
  name = fields.Str(required=True)
  continent = fields.Str(required=True)
  region = fields.Str(required=True)
  population = fields.Int(dump_only=True)
