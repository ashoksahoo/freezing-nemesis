from app import db
from datetime import datetime
from werkzeug import generate_password_hash, check_password_hash

ROLE_USER = 0
ROLE_ADMIN = 1

# Standard Databases
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60))
    pwdhash = db.Column(db.String())
    email = db.Column(db.String(60))
    activate = db.Column(db.Boolean)
    created = db.Column(db.DateTime)
 
    def __init__(self, username, password, email):
        self.username = username
        self.pwdhash = generate_password_hash(password)
        self.email = email
        self.activate = False
        self.created = datetime.utcnow()
 
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)
 

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # comments = db.relationship('Comment', backref = 'post_id', lazy = 'dynamic')

    def __repr__(self):
        return '<Post %r>' % (self.body)


###############


# class Comment(db.Model):
  #   id = db.Column(db.Integer, primary_key = True)
  #   text = db.Column(db.String(140))
  #   timestamp = db.Column(db.DateTime)
  #   post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

  #   def __repr__(self):
		# return '<Comment %r>' % (self.body)
