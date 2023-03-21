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