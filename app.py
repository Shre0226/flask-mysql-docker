import os
from flask import Flask, render_template
from flaskext.mysql import *      # For newer versions of flask-mysql 
# # from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__, template_folder='templates')
app.debug = True

mysql = MySQL()

# mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mypassword'
app.config['MYSQL_DATABASE_DB'] = 'webapp'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)

conn = mysql.connect()


cursor = conn.cursor()

@app.route("/")
def main():
    return render_template('welcome.html')

@app.route('/hru')
def hello():
    return render_template('hru.html')

@app.route('/db')
def read():
    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchall()
    return render_template('con.html', posts=row)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)