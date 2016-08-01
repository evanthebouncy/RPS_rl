# A SIMPLE REINFORCEMENT LEARNING AGENT FOR ROCK PAPER SISSORS

A simple personal project to brush up RL using rock paper sissor playing

## States

We consider the simple state of the past 1 exchanges, i.e. [(R,P)] are past exchange
where player 1 threw Rock, while player 2 threw Paper


## Actions

An action is either R or P or S

## Q Table

The state , action pairs are stored in a dictionary, all values initialized to 0.0

## Q learning

The standard bellman update was applied: 

The new Q value for a state/value pair is the current reward (win / lose) plus the discounted best future reward (argmaxing the action)

this new Q value is diffed with the old Q value, and a small fraction of it is updated to the Q value

