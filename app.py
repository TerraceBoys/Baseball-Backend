#!.env/bin/python
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/baseball'
CORS(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

class GameState(db.Model):
	id = db.Column('gs_id', db.Integer, primary_key = True)
	score1 = db.Column('gs_score_1', db.Integer, default = 0)
	score2 = db.Column('gs_score_2', db.Integer, default = 0)
	inning = db.Column('gs_inning', db.Integer, default = 1)
	batting = db.Column('gs_batting', db.Integer, default = 0)
	base1 = db.Column('gs_base_1', db.Integer, default = 0)
	base2 = db.Column('gs_base_2', db.Integer, default = 0)
	base3 = db.Column('gs_base_3', db.Integer, default = 0)
	strikes = db.Column('gs_strikes', db.Integer, default = 0)
	outs = db.Column('gs_outs', db.Integer, default = 0)

def __init__(self, score1, score2, inning, batting, base1, base2, base3, strikes, outs):
   self.score1 = score1
   self.score2 = score2
   self.inning = inning
   self.batting = batting
   self.base1 = base1
   self.base2 = base2
   self.base3 = base3
   self.strikes = strikes
   self.outs = outs

class GameStateSchema(ma.ModelSchema):
	class Meta:
		model = GameState

game_state_schema = GameStateSchema()
game_state = GameState.query.order_by('-gs_id').first()

@app.route('/')
def index():
	return "Hello World"

@app.route('/baseball')
def baseball():
    return "Welcome to Baseball with the Terrace Boys!"

@app.route('/baseball/new-game')
def new_game():
	global game_state
	game_state = GameState()
	
	return write_game_state()
    
@app.route('/baseball/game-state/<int:gs_id>')
def get_game_state(gs_id):
	global game_state
	game_state = GameState.query.filter_by(id = gs_id).first()
	
	return jsonify(game_state_schema.dump(game_state).data)

@app.route('/baseball/game-state/current')
def current_game_state():
	global game_state
	game_state = GameState.query.order_by('-gs_id').first()
	
	return jsonify(game_state_schema.dump(game_state).data)

@app.route('/baseball/out/<int:gs_id>')
def out(gs_id):
	global game_state
	if gs_id != game_state.id:
		game_state = GameState.query.filter_by(id = gs_id).first()

	incr_out()

	return write_game_state()

@app.route('/baseball/strike/<int:gs_id>')
def strike(gs_id):
	global game_state
	if gs_id != game_state.id:
		game_state = GameState.query.filter_by(id = gs_id).first()

	if game_state.strikes == 2:
		game_state.strikes = 0
		incr_out()
	else:
		game_state.strikes+=1

	return write_game_state()

def write_game_state():
	db.session.add(game_state)
	db.session.commit()

	return jsonify(game_state_schema.dump(game_state).data)

def incr_out():
	global game_state
	if game_state.outs == 2:
		game_state.outs = 0
		incr_inning()
	else:
		game_state.outs+=1

def incr_inning():
	global game_state
	if game_state.batting:
		game_state.inning+=1
		game_state.batting = 0
	else:
		game_state.batting = 1


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=6003)
