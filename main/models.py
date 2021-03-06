from datetime import datetime
from werkzeug.exceptions import default_exceptions
from main import db, login_manager 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(20), unique=True, nullable=False)
    l_name = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=True, default='Images/user_photos/default.jpg')
    password = db.Column(db.String(60), nullable=False)
    notes = db.relationship('Note', backref='author', lazy=True)

    def __repr__(self):
      return f'User: {self.f_name} {self.l_name}\nEmail: {self.email}'

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

