from marshmallow import Schema, fields, validate
from marshmallow_enum import EnumField

from models.enums import CarBrands
from schemas.validators import validate_year_range


class CreateCarSchema(Schema):
    class Meta:
        ordered = True

    brand = EnumField(CarBrands, by_value=True)
    description = fields.String(required=True, validate=validate.Length(max=100))
    year = fields.Integer(required=True, validate=validate_year_range)
    image = fields.String(required=True, validate=validate.Length(max=255))
    price = fields.Integer(required=True)


class GetCarSchema(Schema):
    class Meta:
        ordered = True

    id = fields.Integer()
    user_id = fields.Integer()
    brand = EnumField(CarBrands, by_value=True)
    description = fields.String()
    year = fields.Integer()
    image = fields.String()
    price = fields.Integer()
