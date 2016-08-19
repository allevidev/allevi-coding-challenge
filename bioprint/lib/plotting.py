import matplotlib
import os
import uuid

import matplotlib.pyplot as plt

matplotlib.use('Agg')

IMG_DIR= os.path.dirname(__file__) + "/../static/"

def plot_alive(xlabel, x_vals=[], y_vals=[]):
  fig = plt.figure()
  fig.suptitle('alive percent x ' + xlabel, fontsize=14, fontweight='bold')

  ax = fig.add_subplot(111)
  fig.subplots_adjust(top=0.85)
  ax.set_title('axes title')

  ax.set_xlabel(xlabel)
  ax.set_ylabel('alive percent')

  ax.plot(x_vals, y_vals, 'o')

  filename = str(uuid.uuid4()) + ".png"
  plt.savefig(IMG_DIR + filename, dpi=72)
  return "/static/" + filename