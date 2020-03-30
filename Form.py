from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Choose(FlaskForm):
    scan_file = SubmitField('Scan a File')
    scan_folder = SubmitField('Scan a Folder')
