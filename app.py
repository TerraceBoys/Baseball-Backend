#!Baseball_env/bin/python
from flask import Flask
from flask_cors import CORS, cross_origin
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
CORS(app)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'baseball'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/')
def index():
    return "Welcome to Baseball with the Terrace Boys!"

@app.route('/new-game')
def new_game():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO game_state (gs_id) VALUES(NULL)")
    cursor.execute("SELECT LAST_INSERT_ID()")
    data = cursor.fetchone()
    print data 
    conn.commit()

    return str(data[0])

@app.route('/game-state/current')
def current_game_state():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game_state ORDER BY gs_id DESC LIMIT 0, 1")
    data = cursor.fetchone()

    return str(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6003)
