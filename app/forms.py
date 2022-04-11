from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed


class UploadForm(FlaskForm):
    description = TextAreaField('description',validators = [DataRequired()])
    photo = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')])
    