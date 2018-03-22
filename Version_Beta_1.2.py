"""Rock Paper Scissors game."""
import random as r

def rock_paper_scissors():    
    """List of possible win conditions."""
    win_list = [('ROCK', 'SCISSORS'),  # Rock beats Scissors
                ('SCISSORS', 'PAPER'),  # Scissors beats paper
                ('PAPER', 'ROCK')]  # Paper beats rock   
    cpu_list = {'ROCK': 'PAPER', 'PAPER':'SCISSORS', 'SCISSORS':'ROCK'}  #List of posibble options        
    selection_list = ['ROCK', 'SCISSORS', 'PAPER']  #List of posibble options to choose 
    stats = {'player':0, 'computer':0, 'ties':0} #Tracks wins,losses and ties   
    outcome = ['WIN', 'DRAW', 'LOSS']
    def game_end(): 
        """Ends the game when either the computer or player has 5 wins."""
        end = 5 #No of wins reuqired to end game
        if stats['player'] == end: 
            print('You have won! Well done!') #Player has won
            return True
        elif stats['computer'] == end:
            print('You have lost! Better luck next time!') #Player has lost
            return True
        else:
            return False      
    def display_stats():
        """Displays number of wins, draws and losses."""
        display = ("            Stats        " #Prints out updated stats after every game is played
                   "\n Player | Computer | Ties"
                   "\n    {player}        {computer}        {ties}"
                   "\n                    ".format(**stats))
        return display   
    def rules():
        """Explains the rules of rock paper scissors"""
        rules = ('\n You choose an option between Rock, Paper and Scissors.\n'
                 '\n       *Rock crushes Scissors'
                 '\n       *Scissors cuts Paper'
                 '\n       *Paper wraps Rock'
                 '\n The first to 5 wins wins the game!')
        return rules        
    def introduction():  
        """Displays introductory message and checks player is ready to play."""
        welcome = ('Welcome to this Rock, Paper and Scissors game!\n'
                   '\n This is a simple game with the following rules:')    
        print(welcome, rules())
        ready = input('Are you ready? (type YES to play) ')
        ready = ready.upper()
        if ready == 'YES':
            play_game()
        else:
            print('Too scared I see maybe you can pluck up the courage next time')
        return rules                        
    def play_game():
        """Begins the game ."""
        finished = False 
        game = 0  
        while finished is False:
            def computer_move(): 
                """Decides how the computer will choose a move."""
                if game == 0:
                    move = 'PAPER' #Rock is most likely people's first choice computer uses this 
                elif player_selection in selection_list: 
                    if result == outcome[0]: #Player more likely to choice a winning choice twice 
                        move = cpu_list[player_selection]
                    elif result == outcome[1] or outcome[2]: #player more likely to change with a loss or draw
                        n = 0
                        for choice in selection_list:
                            if choice == player_selection:
                                move = win_list[n][r.randint(0, 1)]
                            else:
                                n += 1
                else:
                    move = r.choice(selection_list)
                return move 
            computer_selection = computer_move() 
            player_selection = input('Your selection is: {} '.format(selection_list)) 
            player_selection = player_selection.upper() 
            #Checks valid input             
            if player_selection in selection_list:     
                game += 1
                match = (player_selection, computer_selection)              
                if player_selection == computer_selection:
                    print("It's a tie you both chose {}".format(player_selection))
                    stats['ties'] += 1
                    result = outcome[1]
                elif match in win_list:
                    print("{} beats {} so you win!".format(player_selection, computer_selection))
                    stats['player'] += 1
                    result = outcome[0]
                else:
                    print("{} is beaten by {} so you lose!".format(player_selection, computer_selection))
                    stats['computer'] += 1
                    result = outcome[2]
                #Displays after each game
                print(display_stats())
                finished = game_end()
                print('This is game number: ' + str(game))                                     
            elif player_selection == 'HELP':
                print(rules())
            elif player_selection == 'EXIT':
                print('Too weak to continue I see')
                finished = True
            else:
                print('Invalid input if you need help type help')            
    introduction()        
 
rock_paper_scissors()              
                    