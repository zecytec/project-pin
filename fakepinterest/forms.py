from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    senha = PasswordField('senha', validators=[DataRequired(), ])
    botao_confirmacao = SubmitField('fazer o login')

class FormCriarConta(FlaskForm):
    username = StringField('username', validators=[DataRequired()]) 
    email = StringField('email', validators=[DataRequired(message='O e-mail é obrigatório.'), Email(message='Use um formato válido de e-mail.')])  
    senha = PasswordField('senha', validators=[DataRequired(), Length(6 , 20)]) 
    confirmacao_senha = PasswordField('confirmação de senha', validators=[DataRequired(), EqualTo('senha')])
    botao_confirmacao = SubmitField('criar conta')
    
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('email já cadastrado, faça login para continuar')