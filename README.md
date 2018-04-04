# RockPaperScissors

Introduction:

The aim of this project was to develop a rock paper scissors game whereby the computer was able to beat the player more than it lost.
This was achieved thanks to the effort of my poor family who had to play this game 100's of times to test if it worked.
The results from testing 400 games from 2 family members where as follows:

Computer - 166

Player - 119 

Draws - 115 

For more information on the testing feel free to read the testing section.

Background

In order to develop a computer algorithm to beat players, I needed to find the optimal strategies for playing. After some research I found three patterns of players which could be exploited these were:
1. The player is more likely to choose rock in the first game.
2. If the player wins then the player is more likely to make the same choice in the next game.
3. If the player loses then the player is more likely to change in the next game.

These will be used to predict and counter the player's future moves.

Testing 

So after successfully implementing the three basic strategies I tested the program which worked well initially, however, I encountered several issues:
1. The computer was deterministic and hence predictable by a player with enough experience.
2. Several simple strategies existed to beat the computer including (Repeating the same choice endlessly or cycling through (rock, scissors, papers))

So to counter these things I made some modifications:
1. Implemented a 30% chance of computer choosing randomly.
2. Implementing a pattern spotting algorithm to detect and predict patterns in players moves.

As a result of these changes, the games were far less predictable and there were no obvious repeating patterns that were able to consistently beat the machine. Once I was satisfied with these changes I tested the computer over the course of 400 games against two different opponents. The results were:

Computer - 166

Player - 119 

Draws - 115 

So the computer won more games but was it significantly better than just random? 

Short answer... yes it was.

Long answer...time for the technical bit. So to answer this a one-tailed statistical test at the 10% significance level was performed with the null hypothesis is that the computer is no better than random. The probability of this result was 0.2% if the games were random and as such can reject the null hypothesis and I can say that my computer is better than a purely random algorithm. 

Conclusion

Overall the project was a success as I was able to create a computer algorithm capable of beating human players over a sufficient number of games. 

Possible improvements could include:
1. Integrating this using the pygame module into a web application.
2. Using all of the players moves history to pick up more player patterns such as tendencies for rock etc...
3. Saving users player history to create a database of move history to help predict player tendencies.



