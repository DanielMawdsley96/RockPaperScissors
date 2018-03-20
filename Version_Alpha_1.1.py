import random

#List of possible win conditions
Win_List = [('ROCK', 'SCISSORS'),  # Rock beats Scissors
            ('SCISSORS', 'PAPER'),  # Scissors beats paper
            ('PAPER', 'ROCK')]  # Paper beats rock   

#List of posibble options to choose
selection_list = ['ROCK', 'PAPER', 'SCISSORS'] 

#Dictionary for tracking number of wins,losses and ties
Stats = {'player':0, 'computer':0, 'ties':0}

def GameEnd(): #Ends the game when either the computer or player has 5 wins
    end = 5 #No of wins reuqired to end game
    if Stats['player'] == end: 
        print('You have won! Well done!')
        return True
    elif Stats['computer'] == end:
        print('You have lost! Better luck next time!')
        return True
    else:
        return False
 
def intro():
    print('Welcome to this Rock, Paper and Scissors game!\n'
          '\n This is a simple game with the following rules:'
          '\n You choose an option between Rock, Paper and Scissors.\n'
          '\n       *Rock crushes Scissors'
          '\n       *Scissors cuts Paper'
          '\n       *Paper wraps Rock'
          '\n The first to 5 wins wins the game!')
    ready = input('Are you ready? (type YES to play) ')
    ready = ready.upper()
    if ready == 'YES':
        PlayGame()
    else:
        print('Too scared I see maybe you can pluck up the courage next time')
          
def PlayGame():
        Finished = False
        while Finished == False:
            player_selection = input('Your selection is: {} '.format(selection_list)) #Player enters their move
            player_selection = player_selection.upper()
            
            if player_selection in selection_list: #Checks valid input 
                computer_selection = random.choice(selection_list) #Computers randomly generated move
            
                match = (player_selection, computer_selection) #Converts player and computer move to tuple to compare to the win list
            
                if player_selection == computer_selection:
                    print("It's a tie you both chose {}".format(player_selection))
                    Stats['ties'] += 1
                elif match in Win_List:
                    print("{} beats {} so you win!".format(player_selection, computer_selection))
                    Stats['player'] += 1
                else:
                    print("{} beats {} so you lose!".format(computer_selection, player_selection))
                    Stats['computer'] += 1
                print("            Stats        " #Prints out updated stats after evry game is played
                      "\n Player | Computer | Ties"
                      "\n    {player}        {computer}        {ties}"
                      "\n                    ".format(**Stats))
                Finished = GameEnd()
        
intro()       
    
    
    
    


