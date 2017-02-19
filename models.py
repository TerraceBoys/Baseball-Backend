from app import db
from app import ma

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
