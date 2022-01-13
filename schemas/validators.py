from datetime import datetime

from marshmallow import ValidationError


def validate_year_range(value):
    current_year = datetime.now().year
    if not (1886 <= value <= current_year):
        raise ValidationError(f'Year must be in range 1886 - {current_year}.')


def username_starts_with_capital_letter(username):
    if username[0].islower():
        raise ValidationError('The username must start with capital letter.')
