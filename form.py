from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField,SearchField
from wtforms.validators import DataRequired, Length


class New(FlaskForm):
    name=StringField(label="Name", validators=[DataRequired(), Length(min=4, max=16)])
    contacts=IntegerField(label='Contact', validators=[DataRequired()])
    submit=SubmitField(label='Save')
    
class Box(FlaskForm):
    search_name=StringField('Name')
    submit=SubmitField('Search')
    