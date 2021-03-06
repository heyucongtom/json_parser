
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'LPAREN MINUS NUMBER PLUS RPARENexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'NUMBER':([0,5,6,7,],[4,4,4,4,]),'LPAREN':([0,5,6,7,],[5,5,5,5,]),'$end':([1,2,3,4,9,10,11,],[0,-3,-4,-5,-1,-2,-6,]),'PLUS':([1,2,3,4,8,9,10,11,],[6,-3,-4,-5,6,-1,-2,-6,]),'MINUS':([1,2,3,4,8,9,10,11,],[7,-3,-4,-5,7,-1,-2,-6,]),'RPAREN':([2,3,4,8,9,10,11,],[-3,-4,-5,11,-1,-2,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,5,],[1,8,]),'term':([0,5,6,7,],[2,2,9,10,]),'factor':([0,5,6,7,],[3,3,3,3,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','simple_algo_parser.py',6),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','simple_algo_parser.py',10),
  ('expression -> term','expression',1,'p_expression_term','simple_algo_parser.py',14),
  ('term -> factor','term',1,'p_term_factor','simple_algo_parser.py',18),
  ('factor -> NUMBER','factor',1,'p_factor_num','simple_algo_parser.py',22),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','simple_algo_parser.py',26),
]
