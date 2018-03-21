"""Rock Paper Scissors game."""
import random as r
def rock_paper_scissors():    
    """List of possible win conditions."""
    win_list = [('ROCK', 'SCISSORS'),  # Rock beats Scissors
                ('SCISSORS', 'PAPER'),  # Scissors beats paper
                ('PAPER', 'ROCK')]  # Paper beats rock   
    cpu_list = {'ROCK': 'PAPER', 'PAPER':'SCISSORS', 'SCISSORS':'ROCK'}  #List of posibble options        
    selection_list = ['ROCK', 'SCISSORS', 'PAPER']  #List of posibble options to choose 
    choices = {'R':'ROCK', 'S':'SCISSORS', 'P':'PAPER'}
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
        ready = input('Are you ready? (type YES to play) \n')
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
        history = [0, 1, 2, 3, 4, 5]
        while finished is False:
            def computer_move(): 
                """Decides how the computer will choose a move."""
                rand = r.randint(1,10)
                #test 1 
                if game == 0:
                    move = 'PAPER' #Rock is most likely people's first choice 
                #test 2
                elif rand < 4: #Element of randomness to prevent counterstratergies
                    move = r.choice(selection_list)
                    print('This was a random move!')
                #test 3 
               
                #test 4
                elif player_selection in selection_list: 
                    #Tests repetition of length 3
                    recent_history = range(1,4)
                    repetition = 0
                    for a in recent_history: 
                        if history[-a] == history[-a-3]:
                            repetition += 1
                    if repetition == 3:
                        move = cpu_list[history[-3]]
                    #Tests repetition of length 2
                    repetition = 0
                    for a in recent_history: 
                        if history[-a] == history[-a-2]:
                            repetition += 1
                    if repetition == 3:
                        move = cpu_list[history[-2]]
                      
                    elif (history[-1] == history[-2] == history[-3]) or result == outcome[0]: 
                        move = cpu_list[player_selection]  
                        
                    elif (history[-1] == history[-2]) or result == outcome[2]: #player more likely to change with a loss 
                        n = 0
                        for choice in selection_list:
                            if choice == player_selection:
                                move = win_list[n][1]
                            else:
                                n += 1
                    #test 4
                    elif result == outcome[1]: #Choices random if it's a draw
                        move = r.choice(selection_list)
                else:
                    move = r.choice(selection_list)
                return move 
            
            computer_selection = computer_move() 
            player_selection = input("Type R for rock, P for paper and S for scissors: \n\n") 
            player_selection = player_selection.upper() 
            if len(player_selection) == 1: #Converts r, p, s to rock paper scissors
                if player_selection in choices:
                    player_selection = choices[player_selection]
            #Checks valid input             
            if player_selection in selection_list:     
                game += 1
                match = (player_selection, computer_selection)              
                if player_selection == computer_selection:
                    print("\n       ----  TIE! ---- \n"  
                          '\n             ¬_¬       \n')
                    stats['ties'] += 1
                    result = outcome[1]
                elif match in win_list:
                    print("\n       ----  WIN! ---- \n" 
                          "\n            ^ O ^   \n")
                    stats['player'] += 1
                    result = outcome[0]
                else:
                    print("\n      ----  LOSS! ---- \n"
                          "\n             \ /              "
                          "\n             . .              "
                          "\n              O               ")
                    stats['computer'] += 1
                    result = outcome[2]
                #Displays after each game
                history.append(player_selection)
                print(display_stats())
                print('Game: ' + str(game))
                if game == 100:
                    print('\n Thank you for playing! You can stop now \n')                                     
            elif player_selection == 'HELP':
                print(rules())
            elif player_selection == 'EXIT':
                print('Too weak to continue I see')
                finished = True
            else:
                print('Invalid input if you need help type help')            
    introduction()        
 
rock_paper_scissors()              
                    