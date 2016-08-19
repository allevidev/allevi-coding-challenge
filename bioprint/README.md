This simple webapp allows you to view alive percent by the various
print info parameters.  With more time, I'd add correlation coefficients and
some other interesting statistics.  With even more time, I'd try to create
a model to maximize alive percentage given the print info parameters. 

The code is written in Python using Flask.  To run it:
- create a virtualenv and pip install -r requirements.txt
- run python bioprint/util/init_db.py bioprint-data.json
- run ./bioprint/run.sh

You should then be able to log into the webapp at http://localhost:5000.
