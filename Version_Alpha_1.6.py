import random

def RockPaperScissors():
    
    #List of possible win conditions
    Win_List = [('ROCK', 'SCISSORS'),  # Rock beats Scissors
                ('SCISSORS', 'PAPER'),  # Scissors beats paper
                ('PAPER', 'ROCK')]  # Paper beats rock   
    
    #List of posibble options to choose
    selection_list = ['PAPER', 'ROCK', 'SCISSORS'] 
    
    #Dictionary for tracking number of wins,losses and ties
    Stats = {'player':0, 'computer':0, 'ties':0}
    
    #Ends the game when either the computer or player has 5 wins
    def GameEnd(): 
        end = 5 #No of wins reuqired to end game
        if Stats['player'] == end: 
            print('You have won! Well done!') #Player has won
            return True
        elif Stats['computer'] == end:
            print('You have lost! Better luck next time!') #Player has lost
            return True
        else:
            return False
      
    #Displays number of wins, draws and losses 
    def DisplayStats():
        Display = ("            Stats        " #Prints out updated stats after every game is played
                   "\n Player | Computer | Ties"
                   "\n    {player}        {computer}        {ties}"
                   "\n                    ".format(**Stats))
        return Display
    
    #Displays introductory message and checks player is ready to play
    def introduction():
        rules = ('Welcome to this Rock, Paper and Scissors game!\n'
                '\n This is a simple game with the following rules:'
                '\n You choose an option between Rock, Paper and Scissors.\n'
                '\n       *Rock crushes Scissors'
                '\n       *Scissors cuts Paper'
                '\n       *Paper wraps Rock'
                '\n The first to 5 wins wins the game!')
        print(rules)
        ready = input('Are you ready? (type YES to play) ')
        ready = ready.upper()
        if ready == 'YES':
            PlayGame()
        else:
            print('Too scared I see maybe you can pluck up the courage next time')
        return rules
       
    # Begins the game                  
    def PlayGame():
            Finished = False 
            Result = 0
            while Finished == False:
                player_selection = input('Your selection is: {} '.format(selection_list)) #Player enters their move
                player_selection = player_selection.upper()
                 
                def ComputerAI(): #Decides how the computer will choice  
                    if Result == 'WIN':
                        if player_selection == 'ROCK':
                            move = 'PAPER'
                        elif player_selection == 'PAPER':
                             move = 'SCISSORS'
                        elif player_selection == 'SCISSORS':
                             move = 'ROCK'
                    else:
                        move = random.choice(selection_list)
                    return move 
                
                if player_selection in selection_list: #Checks valid input 
                    computer_selection = ComputerAI() #Computers generated move
                
                    match = (player_selection, computer_selection) #Converts player and computer move to tuple to compare to the win list
                
                    if player_selection == computer_selection:
                        print("It's a tie you both chose {}".format(player_selection))
                        Stats['ties'] += 1
                        Result = 'TIE'
                    elif match in Win_List:
                        print("{} beats {} so you win!".format(player_selection, computer_selection))
                        Stats['player'] += 1
                        Result = 'WIN'
                    else:
                        print("{} beats {} so you lose!".format(computer_selection, player_selection))
                        Stats['computer'] += 1
                        Result = 'LOSS'
                    
                    print(DisplayStats())
                    Finished = GameEnd()
                    
                    print(Result)
                  
                elif player_selection == 'HELP':
                    print('You are a loser')
                    
                elif player_selection == 'EXIT':
                    Finished = True
                    
                else:
                    print('Invalid input do you need help?') 
                
                    

                            
    introduction()
    
RockPaperScissors()
            
            
                
      

