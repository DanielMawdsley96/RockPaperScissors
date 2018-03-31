"""Rock Paper Scissors game."""
import random as r
def rock_paper_scissors():    
    """List of possible win conditions."""
    win_list = [('ROCK', 'SCISSORS'),  # Rock beats Scissors
                ('SCISSORS', 'PAPER'),  # Scissors beats paper
                ('PAPER', 'ROCK')]  # Paper beats rock   
    counter_play = {'ROCK': 'PAPER', 'PAPER':'SCISSORS', 'SCISSORS':'ROCK'}  #List of counter plays        
    selection_list = ['ROCK', 'SCISSORS', 'PAPER']  #List of posibble options to choose 
    choices = {'R':'ROCK', 'S':'SCISSORS', 'P':'PAPER'}
    stats = {'player':0, 'computer':0, 'ties':0} #Tracks wins,losses and ties   
    outcome = ['WIN', 'DRAW', 'LOSS']
    def game_end(): 
        """Ends the game when either the computer or player has 5 wins."""
        end = 5 #No of wins required to end game
        if stats['player'] == end: 
            print('\nYou won! You must of cheated!') #Player has won
        elif stats['computer'] == end:
            print('\nPuny human I have defeated you! ' #Player has lost
                  '\nPlay me again if you dare!')
        return stats['player']  == end or stats['computer']  == end 
    def display_stats():
        """Displays number of wins, draws and losses."""
        display = ("            Stats        " #Prints out updated stats after every game is played
                   "\n Player | Computer | Ties"
                   "\n    {player}        {computer}        {ties}"
                   "\n                    ".format(**stats))
        return display   
    def rules():
        """Explains the rules of rock paper scissors"""
        rules = ('\nYou choose an option between Rock, Paper Scissors.\n'
                 '\n       *Rock crushes Scissors'
                 '\n       *Scissors cuts Paper'
                 '\n       *Paper wraps Rock\n'
                 '\nThe first to 5 wins wins the game!'
                 '\nIf you wish to exit or need help type exit or help\n')
        return rules        
    def introduction():  
        """Displays introductory message and checks player is ready to play."""
        welcome = ('Welcome to this Rock, Paper and Scissors game!\n'
                   '\nThis is a simple game with the following rules:')    
        print(welcome, rules() + '\nYou will be facing a fearsome machine that does not like to lose!')
        ready = input('\nHello weak human if you think you can defeat me then type YES: \n')
        ready = ready.upper()
        if ready == 'YES':
            print('\nPuny human prepare to be defeated! \n')
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
                random_game = r.randint(1, 10)
                #test 1 
                if game == 0:
                    move = 'PAPER' #Rock is most likely people's first choice 
                #test 2
                elif random_game < 4: #30% chance of randomness to prevent counterstratergies
                    move = r.choice(selection_list)
                #test 3 
               
                #test 4
                elif player_selection in selection_list: 
                    recent = range(1,7)
                    recent_history = []
                    repetition = 0
                    repetition_length = 3 #length of the repeating pattern
                    for games in recent: #Stores last 6 moves in recent history
                        recent_history.append(history[-games])   
                    while repetition_length > 0: #Checks for patterns in recent moves 
                        for games in range(1, 4): 
                            if recent_history[games] == recent_history[games-repetition_length]:
                                repetition += 1
                        if repetition == 3: #condition for a pattern in recent history
                            move = counter_play[history[-repetition_length]]
                            repetition_length = 0
                        else:
                            repetition = 0
                            repetition_length -= 1
                            if repetition_length == 0: #if no patterns found 
                                move = 'None'
                    if move == 'None':                       
                        if result == outcome[0]:
                            move = counter_play[player_selection]                        
                        elif  result == outcome[2]: #player more likely to change with a loss 
                            n = 0
                            for choice in selection_list:
                                if choice == player_selection:
                                    move = win_list[n][1]
                                else:
                                    n += 1
                    #test 4
                    elif result == outcome[1]: #Choices random if it's a draw
                        move = r.choice(selection_list)
                else: #If player choice invalid then next valid is random
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
                          '\n             ¬_¬       \n'
                          '\nWaste of my precious time play again and I will crush you!\n')
                    stats['ties'] += 1
                    result = outcome[1]
                elif match in win_list:
                    print("\n       ----  WIN! ---- \n" 
                          "\n            ^ O ^   \n"
                          "\nA human win? You just got lucky!\n")
                    stats['player'] += 1
                    result = outcome[0]
                else:
                    print("\n      ----  LOSS! ---- \n"
                          "\n             \ /              "
                          "\n             . .              "
                          "\n              O               \n"
                          "\nPoor choice human I saw that coming!\n")
                    stats['computer'] += 1
                    result = outcome[2]
                #Displays after each game
                history.append(player_selection)
                
                print(display_stats())
                print('Game: ' + str(game))
                finished = game_end()
                if game == 100:
                    print('\n Thank you for playing! You can stop now \n') 
            elif player_selection == 'HELP':
                print(rules())
            elif player_selection == 'EXIT':
                print('Pathetic! You do not possess the strength to beat me!')
                finished = True
           
            else:
                print('Invalid input if you need help or wish to leave type help or exit')            
    introduction()        
 
rock_paper_scissors()              
                    
