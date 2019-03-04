from fakebook_pac import db
from datetime import datetime

class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	m_name = db.Column(db.String(20),nullable=False)
	m_email=db.Column(db.String(100),nullable=False,unique=True)
	m_profile_pic = db.Column(db.String(20),nullable=False,default='default.jpg')
	m_password= db.Column(db.String(60),nullable=False)
	m_gender = db.Column(db.String(7),nullable=False,default='Male')
	m_posts = db.relationship('Post',backref='author',lazy=True)


class Post(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	m_content_type = db.Column(db.String(100),nullable=False)
	m_content= db.Column(db.String(100),nullable=False)
	m_date = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
	m_user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

