from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired


class EmailForm(Form):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

class OCBForm(Form):
    agente = StringField('agente', validators=[DataRequired()])
    tipo= StringField('tipo', validators=[DataRequired()])
    descrip= StringField('descrip', validators=[DataRequired()])
    issue= StringField('issue', validators=[DataRequired()])
    culture= StringField('culture', validators=[DataRequired()])
    product= StringField('product', validators=[DataRequired()])
    certified= StringField('certified', validators=[DataRequired()])