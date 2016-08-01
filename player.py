from game import *
import random

# the RPS player, consists of a mover and a updater

rps = ["R","P","S"]

def mk_q_table():
  ret = dict()
  for p1 in rps:
    for p2 in rps:
      for nxt_move in rps:
        ret[((p1,p2),nxt_move)] = 0.0
  for nxt_move in rps:
    ret [(("X","X"), nxt_move)] = 0.0
  return ret

def suggest_move(last_move, q_table):
  keys = [(last_move, mv) for mv in rps]
  values = [(q_table[k], k) for k in keys]
  if random.random() < 0.4:
    return values[random.randint(0,2)]
  else:
    return max(values) 

def get_q_value(state, q_table):
  keys = [(last_move, mv) for mv in rps]
  maxx = max([(q_table[k], k) for k in keys])
  return maxx[0]

def compute_new_q(last_state, move, cur_state, q_table):
  value = get_value(cur_state)
  future_value = get_q_value(cur_state, q_table) * 0.9
  return (last_state, move), value + future_value

def update_q(last_state, move, cur_state, q_table):
#  print "updating!"
  new_q_v = compute_new_q(last_state, move, cur_state, q_table)
  old_q = q_table[(last_state, move)]

  diff = new_q_v[1] - old_q
#  print q_table[(last_state, move)]
  q_table[(last_state, move)] += 0.1 * diff
#  print q_table[(last_state, move)]

q_table = mk_q_table()
last_move = ("X","X")
n_win = 0
n_tie = 0
n_lose = 0
while True:

  # get the users move
  move = raw_input("ur move [R/P/S] ? \n")
  if move not in ["R", "P", "S"]:
    move = "R"

  print "your move was: ", move
  
  ai_move = suggest_move(last_move, q_table)[1][1]

  print "agent move was: ", ai_move

  cur_exchange = (ai_move, move)
  
  if get_value(cur_exchange) == 0.0: 
    print "tie"
    n_tie += 1
  if get_value(cur_exchange) == 1.0: 
    print "u lose!"
    n_lose += 1
  if get_value(cur_exchange) == -1.0: 
    print "u win!"
    n_win += 1

  update_q(last_move, ai_move, cur_exchange, q_table)
  last_move = cur_exchange
  print "win {0}  lose {1}  tie {2}".format(n_win, n_lose, n_tie)



