from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import ValidationError


class RandomNumberForm(FlaskForm):
    min = StringField('min')
    max = StringField('max')

    def validate_min(form, field):
        """Ensure that 'min' is a valid integer."""
        try:
            field.data = int(field.data)
        except (ValueError, TypeError):
            raise ValidationError("The 'min' value must be a valid integer.")

    def validate_max(form, field):
        """Ensure that 'max' is a valid integer and greater than or equal to 'min'."""
        try:
            field.data = int(field.data)
        except (ValueError, TypeError):
            raise ValidationError("The 'max' value must be a valid integer.")

        if form.min.data is not None and field.data < form.min.data:
            raise ValidationError("'Max' value must be greater than or equal to 'min'.")
