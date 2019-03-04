from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,RadioField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from fakebook_pac.dbClasses import User
class SignUpForm(FlaskForm):
	m_name = StringField('Name', validators=[DataRequired(),Length(min=2,max=16)])
	m_email=StringField('Email',validators=[DataRequired(),Email()])
	m_password=PasswordField('Password',validators=[DataRequired(),Length(min=4,max=16)])
	m_val_password=PasswordField('Confirm Password',validators=[DataRequired(),
								EqualTo('m_password')])
	m_gender=RadioField(label='Gender',choices=[('value','Male'),('value2','Female')])
	m_submit=SubmitField('Sign Up')

	def validate_email(self,m_email):
		email_used = User.query.filter_by(m_email=m_email.data).first()
		if email_used:
			raise ValidationError('The Email is taken')

class SignInForm(FlaskForm):
	m_email=StringField('Email',validators=[DataRequired(),Email()])
	m_password=PasswordField('Password',validators=[DataRequired(),Length(min=4,max=16)])
	m_submit=SubmitField('Sign In')
	m_rememberMe=BooleanField('Remember Me')
