"""DATABASE MODELS """
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app import db
#pylint: disable=R0903
class User(UserMixin, db.Model):
    """ USER ACCOUNT DATABASE MODEL """

    __tablename__ = "flasksession-users"

    # User Login infromation
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=True)
    last_login = db.Column(db.DateTime)
    profile_image = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    # Password
    def set_password(self, password):
        """ HASH PASSWORDS """
        self.password = generate_password_hash(password, method="pbkdf2:sha256")

    def check_password(self, password):
        """ CHECK PASSWORDS """
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f"<User id={self.id}, name={self.name},"\
               f"email={self.email}, password={self.password}>"
               
    # User Profile Image
    def get_images(self):
        """ Return images associated with the user """
        return self.profile_image

    def set_profile_image(self, filename):
        """ Add a new image for the user """
        self.profile_image = filename

# Error Log Messages for displaying errors
class Message(db.Model):
    """ ERROR LOGS DATABASE MODEL """
    __tablename__ = "messages"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())

    def __init__(self, content):
        self.content = content
