# RockPaperScissors
Collection of pyhton scripts which play the game of rock, paper scissors. In verisons in the beta the computer ai is designed to beat the opponent using information from a study on rock paper scissors and in the later version is able to recognise patterns in order to predict player moves. 

Introduction:

The aim of this project was to develop a rock paper scissors game wherby the computer was able to beat the player more than it lost.
This was acheived thanks to the effort of my poor family who had to play this game 100's of times to test if it worked.
The results from testing 400 games from 2 family members where as follows:

Computer - 166
\n Player - 119 
\n Draws - 115 

For more information on the testing feel free to reading the testing section.

Background

In order to develop a computer with rock paper scissors stratergies first I found if there any and what these were. After some reseacrh I found several stratergies to improve these were:
1. Player more likely to choose rock on first choice (50% of the time).
2. If the player wins then player more likely to stay the same (50% of the time).
3. If the player loses then they are more likely to change (60% of the time).
I will use these three pieces of data in order to help the computer predict what the player choose.

Testing 

So after successfully implementing the three stratergies discussed earlier I encountered several problems:
1. The computer was deterministic and hence predictable by a player with enough experience.
2. Several simple stratergies existed to beat including (Repeating the same choice endlessly or cycling through (rock, scissors, papers)

So to counter these things I made some modifications:
1. Implemented a 30% chance of computer choosing random.
2. Implementing a pattern spotting algorithem to detect and predict patterns in players moves.




