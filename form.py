from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class UrlForm(FlaskForm):
    url = StringField('Nhập đường dẫn thư mục/tệp:', validators=[DataRequired()],
                      render_kw={"placeholder": "Nhập đường dẫn phù hợp với thư mục cha là /"})
    submit = SubmitField('Scan')
