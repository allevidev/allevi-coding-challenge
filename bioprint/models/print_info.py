from bioprint import db
from bioprint.models.print_data import PrintData

from sqlalchemy.orm import relationship


class PrintInfo(db.Model):
  __tablename__ = 'print_info'
  id = db.Column(db.Integer, primary_key=True)
  
  print_data = relationship('PrintData', back_populates='print_info')

  user_info_id = db.Column(db.Integer, db.ForeignKey("user_info.serial"))
  user_info = relationship('UserInfo', back_populates='print_info')

  crosslinking_enabled = db.Column(db.Boolean)
  crosslinking_duration = db.Column(db.Integer)
  crosslinking_intensity = db.Column(db.Integer)
  input_file =  db.Column(db.String(255))
  output_file = db.Column(db.String(255))
  pressure_extruder1 = db.Column(db.Float)
  pressure_extruder2 = db.Column(db.Float)
  resolution_layer_num = db.Column(db.Integer)
  resolution_layer_height = db.Column(db.Float)
  well_plate = db.Column(db.Integer)
