from marshmallow import fields, Schema

from project.Schemas.director_schema import DirectorSchema
from project.Schemas.genre_schema import GenreSchema


class MovieSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    trailer = fields.Str(required=True)
    year = fields.Int(required=True)
    rating = fields.Float(required=True)
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)