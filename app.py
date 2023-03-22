# Objective: this is for CSPB3308 Lab 10 Render project 
# Name: Mayumi Shimobe
# GitHub ID: Mayumi=GT
# CU ID: mash8545
# Use: this contains a flask with 6 total working routes.
# / Our initial Hello World route
# db_test Which tests the database connection
# db_create Which creates the Basketball table
# db_insert Which inserts the provided information into the Basketball table
# db_select Which queries the data from Basketball and returns a formatted table of information
# db_drop Which drops the Basketball table
# Note from the instructor: before submitting your final product call the db_drop route to ensure that the database used for your render app is empty, so that I can call your routes to test it.
# A link to my github repository containing your app.py file with the required routes: https://github.com/Mayumi-GT/flask-hello-world
# A link to your flask app on render: https://cspb3308-render-lab.onrender.com


import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
  conn = psycopg2.connect("postgres://mash8545_render_user:OAikQEaPWJ0YlxAEgBV5x7wvyd4BoAHQ@dpg-cgd20l7dvk4htnrc2hi0-a/mash8545_render")
  conn.close()
  return "Database Connection Successful"

@app.route('/db_create')
def creating():
  conn = psycopg2.connect("postgres://mash8545_render_user:OAikQEaPWJ0YlxAEgBV5x7wvyd4BoAHQ@dpg-cgd20l7dvk4htnrc2hi0-a/mash8545_render")
  cur = conn.cursor()
  cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
  ''')
  conn.commit()
  conn.close()
  return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
  conn = psycopg2.connect("postgres://mash8545_render_user:OAikQEaPWJ0YlxAEgBV5x7wvyd4BoAHQ@dpg-cgd20l7dvk4htnrc2hi0-a/mash8545_render")
  cur = conn.cursor()
  cur.execute('''
      INSERT INTO Basketball (First, Last, City, Name, Number)
      Values
      ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
      ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
      ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
      ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
      ''')
  conn.commit()
  conn.close()
  return "Basketball Table Successfully populated"

@app.route('/db_select')
def selecting():
  try:
    conn = psycopg2.connect("postgres://mash8545_render_user:OAikQEaPWJ0YlxAEgBV5x7wvyd4BoAHQ@dpg-cgd20l7dvk4htnrc2hi0-a/mash8545_render")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.close()
    response_string=""
    response_string+="<table>"
    for player in records:
      response_string+="<tr>"
      for info in player:
        response_string+="<td>{}</td>".format(info)
      response_string+="</tr>"
    response_string+="</table>"
    return response_string
  except Exception as e:
    return "Error selecting data: " + str(e)

@app.route('/db_drop')
def dropping():
  try:
    conn = psycopg2.connect("postgres://mash8545_render_user:OAikQEaPWJ0YlxAEgBV5x7wvyd4BoAHQ@dpg-cgd20l7dvk4htnrc2hi0-a/mash8545_render")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
  except Exception as e:
    return "Error dropping table: "