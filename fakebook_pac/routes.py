from flask import render_template,url_for,flash,redirect,get_flashed_messages
from fakebook_pac import app,db,bcrypt
from fakebook_pac import Form
from fakebook_pac import dbClasses

posts = [
		{
		'author':'Noam Levy',
		'post': 'some boolshit',
		'date':'',
		},
		{
		'author':'Tom Levy',
		'post': 'some boolshit',
		'date':''
		}
]
@app.route("/")
def home():
    return render_template('home.html',name="Home",posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',name='About')

@app.route("/sign-up",methods=['GET','POST'])
def sign_up():
	form=Form.SignUpForm()
	if form.validate_on_submit():
		print( f"{dbClasses.User.query.filter_by(m_email=form.m_email.data).first()} printed------------------")
		hashed_password = bcrypt.generate_password_hash(form.m_password.data).decode('utf-8')
		user = dbClasses.User(m_name=form.m_name.data,m_email=form.m_email.data,m_password=hashed_password,m_gender=form.m_gender.data)
		db.session.add(user)
		db.session.commit()
		flash('You signed up! You can now sign in','success')			#success is the bootstrap class for the alert
		return redirect(url_for('sign_in'))
	return render_template('signUp.html',name='Sign-Up',form=form)

@app.route("/sign-in",methods=['GET','POST'])
def sign_in():
	form=Form.SignInForm()
	if form.validate_on_submit():
		flash('Welcome Back!','success')			#success is the bootstrap class for the alert
		return redirect(url_for('home'))

	return render_template('signIn.html',name='Sign-In',form=form)

