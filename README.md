# RockPaperScissors

Introduction:

The aim of this project was to develop a rock paper scissors game wherby the computer was able to beat the player more than it lost.
This was acheived thanks to the effort of my poor family who had to play this game 100's of times to test if it worked.
The results from testing 400 games from 2 family members where as follows:

Computer - 166

Player - 119 

Draws - 115 

For more information on the testing feel free to reading the testing section.

Background

In order to develop a computer algorithim with rock paper scissors stratergies first I found if there any and what these were. After some reseacrh I found three patterns of players which could be exploited these were:
1. Player more likely to choose rock on first choice (50% of the time).
2. If the player wins then player more likely to stay the same (50% of the time).
3. If the player loses then they are more likely to change (60% of the time).

I will use these three pieces of data in order to help the computer predict what the player choose.

Testing 

So after successfully implementing the three stratergies discussed earlier I encountered several problems:
1. The computer was deterministic and hence predictable by a player with enough experience.
2. Several simple stratergies existed to beat the computer including (Repeating the same choice endlessly or cycling through (rock, scissors, papers)

So to counter these things I made some modifications:
1. Implemented a 30% chance of computer choosing random.
2. Implementing a pattern spotting algorithm to detect and predict patterns in players moves.

As a result of these changes the games was far less predictable and there were no obvious repeating patterns that were able to consitently beat the machine. Once I was satisfied after these changes I tested the computer over the course of 400 games against two different opponents. The findings were:


Computer - 166

Player - 119 

Draws - 115 

So the computer won more games but was it signifacntly better than just random? 

Time for the techinical bit. So to answer this a one tailed statistical test at the 10% signifcance level was performed with the null hypothesis being that the computer is no better than random. The probability of this result was 0.2% if the games were random and as such can reject the null hypothesis is rejected and I can say that my computer is better than purely random. 

Conclusion

Overall the project was a success as I was able to create a computer algorithim capable of beating human players. 

Possible improvements could include:
1. Integrating this using the pygame module into a web application.
2. Using all of the history to pick up more player patterns such as tendieces for rock etc...
3. Saving users player history to create a database of move mistory to help predict player tendencies.



