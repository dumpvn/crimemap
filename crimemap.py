# -*- coding: utf-8 -*-
"""
crimemap application.
"""
import json
import dbconfig
import dateparser
import datetime

if dbconfig.test:
    from mockdbhelper import MockDBHelper as DBHelper
else:
    from dbhelper import DBHelper

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
DB = DBHelper()
categories = ['mugging', 'break-in']


def format_date(user_date):
    """
    Convert user input date string into datetime object and then convert to YYYY-MM-DD format.
    """
    date = dateparser.parse(user_date)
    try:
        return datetime.datetime.strftime(date, "%Y-%m-%d")
    except TypeError:
        return None

@app.route("/submitcrime", methods=['POST'])
def submitcrime():
    """
    create new crime from user submission.
    user input validation:
        - category in pre-defined categories list
        - location in float format
    """
    category = request.form.get("category")
    if category not in categories:
        return home()
    date = format_date(request.form.get("date"))
    if not date:
        return home('invalid date. please use yyyy-mm-dd format.')
    try:
        latitude = float(request.form.get("latitude"))
        longitude = float(request.form.get("longitude"))
    except ValueError:
        return home()
    description = request.form.get("description")
    DB.add_crime(category, date, latitude, longitude, description)
    return home()

@app.route("/")
def home(error_msg=None):
    try:
        # data = DB.get_all_inputs()
        crimes = DB.get_all_crimes()
        crimes = json.dumps(crimes)
        return render_template("home.html", crimes=crimes, categories=categories, error_msg=error_msg)
    except Exception as e:
        # data = None
        crimes=None

    # return render_template("home.html", data=data)
    # return render_template("home.html", crimes=crimes)

@app.route("/add", methods=["POST"])
def add():
    try:
        data = request.form.get("userinput")
        DB.add_input(data)
    except Exception as e:
        return home()

@app.route("/clear")
def clear():
    try:
        DB.clear_all()
    except Exception as e:
        return home()

if __name__ == '__main__':
    app.run(port=5000, debug=True)
