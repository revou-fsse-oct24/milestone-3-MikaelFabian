# app/utils/validators.py
from marshmallow import Schema, fields, validate, ValidationError

class UserRegistrationSchema(Schema):
    username = fields.Str(
        required=True, 
        validate=[
            validate.Length(min=3, max=50),
            validate.Regexp(r'^[a-zA-Z0-9_]+$')
        ]
    )
    email = fields.Email(required=True)
    password = fields.Str(
        required=True,
        validate=[
            validate.Length(min=8, max=50),
            validate.Regexp(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')
        ]
    )
    first_name = fields.Str(validate=validate.Length(max=50))
    last_name = fields.Str(validate=validate.Length(max=50))

def validate_user_registration(data):
    try:
        schema = UserRegistrationSchema()
        return schema.load(data)
    except ValidationError as err:
        raise APIError(err.messages, status_code=400)