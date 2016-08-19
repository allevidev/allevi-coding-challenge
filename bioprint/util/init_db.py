import json 
import sys

from bioprint import db

from bioprint.models import PrintData
from bioprint.models import PrintInfo
from bioprint.models import UserInfo

db.create_all()

dataset = json.load(open(sys.argv[1]))

user_info = None
cur_serial = -1

for data in dataset:
  try:
    if data['user_info']['serial'] != cur_serial:
      user_info = UserInfo()
      user_info.serial = data['user_info']['serial']
      user_info.email = data['user_info']['email']
      db.session.add(user_info)
      db.session.commit()
      cur_serial = user_info.serial

    print_info = PrintInfo()
    print_info.user_info_id = user_info.serial
    print_info.crosslinking_enabled = \
      data['print_info']['crosslinking']['cl_enabled']
    print_info.crosslinking_duration = \
      data['print_info']['crosslinking']['cl_duration']
    print_info.crosslinking_intensity = \
      data['print_info']['crosslinking']['cl_intensity']
    print_info.input_file = data['print_info']['files']['input']
    print_info.output_file = data['print_info']['files']['output']
    print_info.pressure_extruder1 = data['print_info']['pressure']['extruder1']
    print_info.pressure_extruder2 = data['print_info']['pressure']['extruder2']
    print_info.resolution_layer_num = \
      data['print_info']['resolution']['layerNum']
    print_info.resolution_layer_height = \
      data['print_info']['resolution']['layerHeight']
    print_info.well_plate = data['print_info']['wellplate']
    db.session.add(print_info)
    db.session.commit()

    print_data = PrintData()
    print_data.user_info_id = user_info.serial
    print_data.print_info_id = print_info.id
    print_data.dead_percent = data['print_data']['deadPercent']
    print_data.elasticity = data['print_data']['elasticity']
    print_data.live_percent = data['print_data']['livePercent']
    db.session.add(print_data)
    db.session.commit()

  except Exception, e:
    print "DATA ERROR: {}".format(e)