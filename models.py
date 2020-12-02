from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey
db = SQLAlchemy()

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    status = db.Column(db.Boolean, default=True)
    users = db.relationship('User', secondary="roles_users")


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    birthday = db.Column(db.DateTime)
    profile = db.relationship('Profile', backref="user", lazy=True, uselist=False)
    phones = db.relationship('Phone', backref="user", lazy=True)
    #role_id = db.Column(db.Integer, ForeignKey('roles.id')) #opcion si quiero un solo rol por usuario 
    roles = db.relationship('Role', secondary="roles_users")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "profile": self.profile.serialize(),
            "phones": self.get_phones()
        }

    def get_phones(self):
        return list(map(lambda phone: phone.serialize(), self.phones))


class RoleUser(db.Model):
    __tablename__ = 'roles_users'
    role_id = db.Column(db.Integer, ForeignKey('roles.id'), primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('users.id'), primary_key=True)


class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    bio = db.Column(db.String(300), nullable=True, default="")
    twitter = db.Column(db.String(300), nullable=True, default="")
    facebook = db.Column(db.String(300), nullable=True, default="")
    instagram = db.Column(db.String(300), nullable=True, default="")
    linkedin = db.Column(db.String(300), nullable=True, default="")
    photo = db.Column(db.String(300), nullable=True, default="")
    user_id = db.Column(db.Integer, ForeignKey('users.id'))



class Phone(db.Model):
    __tablename__ = 'user_phones'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(50))
    user_id = db.Column(db.Integer, ForeignKey('users.id'))