import scipy

from flask import Flask
from flask import make_response
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/bioprint.sqlite'
db = SQLAlchemy(app)

from bioprint.models.print_data import PrintData
from bioprint.models.print_info import PrintInfo
from bioprint.models.user_info import UserInfo

from lib.plotting import plot_alive

PLOT_OPTS = [
  'crosslinking_duration',
  'crosslinking_intensity',
  'pressure_extruder1',
  'pressure_extruder2',
  'resolution_layer_num',
  'resolution_layer_height'
]

@app.route('/login')
def login():
 return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
  email = None
  if request.method == "POST":
    email = request.form.get('email')
  elif request.cookies.get('email'):
    email = request.cookies.get('email')

  if email:
    user = db.session.query(UserInfo).filter_by(email=email).first()
    if user:
      resp = make_response(render_template('index.html', user=user,
        plot_opts=PLOT_OPTS))
      resp.set_cookie('email', email)
      return resp

  return redirect(url_for("login"))

@app.route('/plot', methods=['POST'])
def plot():
  email = request.cookies.get('email')
  user = db.session.query(UserInfo).filter_by(email=email).first()
  plot_opt = request.form.get('plot_opt')
  
  x_vals = []
  y_vals = []
  for print_data in user.print_data:
    x_vals.append(getattr(print_data.print_info, plot_opt))
    y_vals.append(print_data.live_percent)

  plot_img = plot_alive(plot_opt, x_vals=x_vals, y_vals=y_vals)

  return render_template('index.html', user=user, plot_opts=PLOT_OPTS, 
    plot_img=plot_img)

def historgram():
  return 1

