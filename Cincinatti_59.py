'''
Predict outcomes for minority groups under ranked choice voting
using four different models of voter behavior.

Enter basic input parameters under Global variables, then run the
code in order to simulate elections and output expected number of poc
candidates elected under each model and model choice.
'''


import numpy as np
from itertools import product, permutations
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random, sys
import compute_winners as cw
from vote_transfers import cincinnati_transfer
from model_details import Cambridge_ballot_type, BABABA, luce_dirichlet, bradley_terry_dirichlet

random.seed(2020)
np.random.seed(2020)
print("Parameters:")


# ## Global variables
poc_share = 0.40
poc_support_for_poc_candidates = 0.76
poc_support_for_white_candidates = 0.24
white_support_for_white_candidates = 0.71
white_support_for_poc_candidates = 0.29
num_ballots = 1000
num_simulations = 100
seats_open = 9
num_poc_candidates = 5
num_white_candidates = 9

print(sys.argv[0])
for s in [
    poc_share, poc_support_for_poc_candidates, poc_support_for_white_candidates,
    white_support_for_white_candidates, white_support_for_poc_candidates, num_ballots,
    num_simulations, seats_open, num_poc_candidates, num_white_candidates]:
    print(s)


#list goes [poc_for_poc, poc_for_white, white_for_poc, white_for_white]
concentration_list = [[0.5]*4, [2,0.5,0.5,0.5], [2,2,2,2], [0.5,0.5,2,2], [1.0]*4]

#PL
poc_elected_luce_dirichlet = []
for i, concentrations in enumerate(concentration_list):
  poc_elected_rcv, _ = luce_dirichlet(
      poc_share = poc_share,
      poc_support_for_poc_candidates = poc_support_for_poc_candidates,
      poc_support_for_white_candidates = poc_support_for_white_candidates,
      white_support_for_white_candidates = white_support_for_white_candidates,
      white_support_for_poc_candidates = white_support_for_poc_candidates,
      num_ballots = num_ballots,
      num_simulations = num_simulations,
      seats_open = seats_open,
      num_poc_candidates = num_poc_candidates,
      num_white_candidates = num_white_candidates,
      concentrations = concentrations,
  )
  poc_elected_luce_dirichlet.append(poc_elected_rcv)


print("\n Plackett-Luce Dirichlet predictions in order:")
for i, c in enumerate(concentration_list[:-1]):
  print("{:.1f}  &".format(np.mean(poc_elected_luce_dirichlet[i])), end=" ")
print("{:.1f} ".format(np.mean(poc_elected_luce_dirichlet[-1])))

#BT
poc_elected_bradley_terry_dirichlet = []
for i, concentrations in enumerate(concentration_list):
  poc_elected_rcv, _ = bradley_terry_dirichlet(
      poc_share = poc_share,
      poc_support_for_poc_candidates = poc_support_for_poc_candidates,
      poc_support_for_white_candidates = poc_support_for_white_candidates,
      white_support_for_white_candidates = white_support_for_white_candidates,
      white_support_for_poc_candidates = white_support_for_poc_candidates,
      num_ballots = num_ballots,
      num_simulations = num_simulations,
      seats_open = seats_open,
      num_poc_candidates = num_poc_candidates,
      num_white_candidates = num_white_candidates,
      concentrations = concentrations,
  )
  poc_elected_bradley_terry_dirichlet.append(poc_elected_rcv)


print("\n Bradley-Terry Dirichlet predictions in order:")
for i, c in enumerate(concentration_list[:-1]):
  print("{:.1f}  &".format(np.mean(poc_elected_bradley_terry_dirichlet[i])), end=" ")
print("{:.1f} ".format(np.mean(poc_elected_bradley_terry_dirichlet[-1])))

#AC
poc_elected_bababa, _  = BABABA(
    poc_share = poc_share,
    poc_support_for_poc_candidates = poc_support_for_poc_candidates,
    poc_support_for_white_candidates = poc_support_for_white_candidates,
    white_support_for_white_candidates = white_support_for_white_candidates,
    white_support_for_poc_candidates = white_support_for_poc_candidates,
    num_ballots = num_ballots,
    num_simulations = num_simulations,
    seats_open = seats_open,
    num_poc_candidates = num_poc_candidates,
    num_white_candidates = num_white_candidates,
    scenarios_to_run = ['A', 'B', 'C', 'D'],
    verbose=False,
)
print("\n Alternating crossover predictions in order:")
for i, c in enumerate(['A', 'B', 'C', 'D']):
  print("{:.1f} &".format(np.mean(poc_elected_bababa[c])), end=" ")
print("{:.1f} ".format(
  np.mean([np.mean(poc_elected_bababa[c]) for c in ['A', 'B', 'C', 'D']]),
))

#CS
poc_elected_Cambridge, _ = Cambridge_ballot_type(
    poc_share = poc_share,
    poc_support_for_poc_candidates = poc_support_for_poc_candidates,
    poc_support_for_white_candidates = poc_support_for_white_candidates,
    white_support_for_white_candidates = white_support_for_white_candidates,
    white_support_for_poc_candidates = white_support_for_poc_candidates,
    num_ballots = num_ballots,
    num_simulations = num_simulations,
    seats_open = seats_open,
    num_poc_candidates = num_poc_candidates,
    num_white_candidates = num_white_candidates,
    scenarios_to_run = ['A', 'B', 'C', 'D'],
)

print("\n Cambridge sampler predictions in order:")
for i, c in enumerate(['A', 'B', 'C', 'D']):
  print("{:.1f} &".format(np.mean(poc_elected_Cambridge[c])), end=" ")
print("{:.1f} ".format(
  np.mean([np.mean(poc_elected_Cambridge[c]) for c in ['A', 'B', 'C', 'D']]),
))
