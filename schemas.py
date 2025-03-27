from marshmallow import Schema, fields

class AnimeQuoteSchema(Schema):
    anime = fields.Str(required=True)
    character = fields.Str(required=True)
    quote = fields.Str(required=True)
