from bioprint import db

from sqlalchemy.orm import relationship


class PrintData(db.Model):
    __tablename__ = 'print_data'
    id = db.Column(db.Integer, primary_key=True)

    user_info_id = db.Column(db.Integer, db.ForeignKey('user_info.serial'))
    print_info_id = db.Column(db.Integer, db.ForeignKey('print_info.id'))
    
    user_info = relationship('UserInfo', back_populates='print_data')
    print_info = relationship('PrintInfo', back_populates='print_data')

    live_percent = db.Column(db.Float)
    dead_percent = db.Column(db.Float)
    elasticity = db.Column(db.Float)

