from bioprint import db

from sqlalchemy.orm import relationship


class UserInfo(db.Model):
  __tablename__ = 'user_info'
  serial = db.Column(db.Integer, primary_key=True, unique=True)

  print_data = relationship('PrintData', back_populates='user_info')
  print_info = relationship('PrintInfo', back_populates='user_info')

  email = db.Column(db.String(255))
