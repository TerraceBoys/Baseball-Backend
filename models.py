from app import db
from app import ma

class GameState(db.Model):
   __tablename__ = 'game_state'
   id = db.Column('gs_id', db.Integer, primary_key = True)
   turns = db.relationship('GameTurn', backref=db.backref('game_turn'))

   def __init__(self, current_turn):
      self.current_turn = current_turn

class GameStateSchema(ma.ModelSchema):
   class Meta:
      model = GameState
      
class GameTurn(db.Model):
   __tablename__ = 'game_turn'
   id = db.Column('gt_id', db.Integer, primary_key = True)
   score1 = db.Column('gt_score_1', db.Integer, default = 0)
   score2 = db.Column('gt_score_2', db.Integer, default = 0)
   inning = db.Column('gt_inning', db.Integer, default = 1)
   batting = db.Column('gt_batting', db.Integer, default = 0)
   base1 = db.Column('gt_base_1', db.Integer, default = 0)
   base2 = db.Column('gt_base_2', db.Integer, default = 0)
   base3 = db.Column('gt_base_3', db.Integer, default = 0)
   strikes = db.Column('gt_strikes', db.Integer, default = 0)
   outs = db.Column('gt_outs', db.Integer, default = 0)
   game_state_id = db.Column(db.Integer, db.ForeignKey('game_state.id'))
   game_state = db.relationship('GameState', foreign_keys=id)

   def __init__(self, previous_turn):
      self.score1 = previous_turn.score1
      self.score2 = previous_turn.score2
      self.inning = previous_turn.inning
      self.batting = previous_turn.batting
      self.base1 = previous_turn.base1
      self.base2 = previous_turn.base2
      self.base3 = previous_turn.base3
      self.strikes = previous_turn.strikes
      self.outs = previous_turn.outs

class GameTurnSchema(ma.ModelSchema):
   class Meta:
      model = GameTurn
   
