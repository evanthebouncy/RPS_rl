## A SIMPLE REINFORCEMENT LEARNING AGENT FOR ROCK PAPER SISSORS ##

A simple personal project to brush up RL using rock paper sissor playing

# States

We consider the simple state of the past 2 exchanges, i.e. [(R,P), (P,S)] are two past exchanges
where player 1 threw Rock then Paper, while player 2 threw Paper and Sissor.

There are 3^4 = 81 total states

# Actions

An action is either R or P or S

# Q values

A table of Q values is stored for every state-action pair, estimating its values.

i.e. ([(R,P), (P,S)], R) is the Q value for a particular past 2 throws, and throwing Rock in the
current state.

all Q values initialized to 1 / 3 then improved

# Q learning


