"""Rock Paper Scissors game designed by Daniel Mawdsley

This program runs a game of rock paper scissors for the first to 5 wins.
The computer decides a move based on rock paper scissors stratergies
along with pattern recognition algorithms to predict what the player will choose."""

import random as r

win_list = [('ROCK', 'SCISSORS'),  # Rock beats Scissors
            ('SCISSORS', 'PAPER'),  # Scissors beats paper
            ('PAPER', 'ROCK')]  # Paper beats rock

counter_play = {'ROCK': 'PAPER', #List of counter plays
                'PAPER':'SCISSORS',
                'SCISSORS':'ROCK'}

selection_list = ['ROCK', 'SCISSORS', 'PAPER'] #List of posibble choices
abbreviations = {'R':'ROCK', 'S':'SCISSORS', 'P':'PAPER'}
stats = {'WINS':0, 'LOSSES':0, 'TIES':0} #Tracks wins, losses and ties
outcome = ['WIN', 'DRAW', 'LOSS']
game = 0
history = [] #Stores player's move history

def game_end():
    """Ends the game when either the computer or player has 5 wins."""

    end = 5 #No of wins required to end game
    if stats['WINS'] == end:
        print('\nYou won! You must of cheated!') #Player has won
    elif stats['LOSSES'] == end:
        print('\nPuny human I have defeated you! ' #Player has lost
              '\nPlay me again if you dare!')
    return stats['WINS'] == end or stats['LOSSES'] == end

def display_stats():
    """Displays number of wins, losses and ties after each game."""

    display = ("         Stats        \n"
               "\n Wins | Losses | Ties"
               "\n---------------------"
               "\n   {WINS}  |    {LOSSES}   |  {TIES}"
               "\n                    ".format(**stats))
    return display

def explain_rules():
    """Explains the rules of rock paper scissors"""

    rules = ('\nYou choose an option between Rock, Paper and Scissors.\n'
             '\n       *Rock crushes Scissors'
             '\n       *Scissors cuts Paper'
             '\n       *Paper wraps Rock\n'
             '\nThe first to 5 wins is the winner!'
             '\nIf you wish to exit or need help type exit or help\n')
    return rules

def introduction():
    """Displays introductory message and checks player is ready to play."""

    welcome = ('Welcome to this Rock, Paper and Scissors game!\n'
               '\nThis is a simple game with the following rules:')
    print(welcome, explain_rules() +
          '\nYou will be facing a fearsome machine that does not like to lose!')

    ready = input('\nHello weak human if you think you can defeat me then type YES: \n')
    ready = ready.upper()

    if ready == 'YES':
        print('\nPuny human prepare to be defeated! \n')
        play_game()
    else:
        print('Too scared I see maybe you can pluck up the courage next time')

    return explain_rules()

def computer_move():
    """Decides how the computer will choose a move based on 7 tests in a hierarchy."""
    random_game = 10*r.random()
    #1.
    if game == 0:
        #Rock is most likely people's first choice
        move = 'PAPER'
    #2.
    elif random_game < 4:
        #30% chance of randomness to deter counterstratergies
        move = r.choice(selection_list)
    #3.
    elif player_selection in selection_list:
        #checks valid move
        pattern = False
        if game > 6:
            #Checks for pattern in last 6 moves
            recent = range(1, 7)
            recent_history = []
            repetition = 0
            repetition_length = 3 #length of the repeating pattern
            for games in recent:
                #Stores last 6 moves in recent history
                recent_history.append(history[-games])
            while repetition_length > 0:
                #Checks for patterns in recent moves
                for games in range(1, 4):
                    if recent_history[games] == recent_history[games-repetition_length]:
                        #condition for one recurring move
                        repetition += 1
                if repetition == 3:
                    #condition for a pattern in recent history
                    move = counter_play[history[-repetition_length]]
                    pattern = True
                    break
                else:
                    repetition = 0
                    repetition_length -= 1
        if pattern is False:
            #4.
            if result == outcome[0]:
                #Winners more likely to throw the same
                move = counter_play[player_selection]
            #5.
            elif result == outcome[2]:
                #Losers are more likely to change
                n = 0
                for choice in selection_list:
                    if choice == player_selection:
                        move = win_list[n][1]
                        break
                    else:
                        n += 1
            #6.
            elif result == outcome[1]:
                #If results is tie choice random
                move = r.choice(selection_list)
    #7.
    else:
        #If player choice invalid then next valid is random
        move = r.choice(selection_list)
    return move

def play_game():
    """Begins the game ."""
    finished = False
    global player_selection
    global game
    global result
    while finished is False:
        #Continues playing untill a win condition or exit
        computer_selection = computer_move()
        #Computer decides first
        player_selection = input("Type R for rock, P for paper and S for scissors: \n\n")
        player_selection = player_selection.upper()

        if player_selection in abbreviations:
            #Converts r, p and s to rock paper scissors
            player_selection = abbreviations[player_selection]

        if player_selection in selection_list:
            #Checks valid input
            game += 1
            history.append(player_selection)
            match = (player_selection, computer_selection)
            #Converts selctions to match to compare in win list
            if player_selection == computer_selection:
                print("\n       ----  TIE! ---- \n"
                      '\n             ¬_¬       \n'
                      '\nWaste of my precious time play again and I will crush you!\n')
                stats['TIES'] += 1
                result = outcome[1]

            elif match in win_list:
                print("\n       ----  WIN! ---- \n"
                      "\n            ^ O ^   \n"
                      "\nA human win? You just got lucky!\n")
                stats['WINS'] += 1
                result = outcome[0]

            else:
                print("\n      ----  LOSS! ---- \n"
                      "\n             \ /              "
                      "\n             . .              "
                      "\n              O               \n"
                      "\nPoor choice human I saw that coming!\n")
                stats['LOSSES'] += 1
                result = outcome[2]

            #Display after each game
            print(display_stats())
            print('Game: ' + str(game))
            #Test for end conditon
            finished = game_end()

            if finished is True:
                #Ask user for rematch
                rematch = input('Would you like a rematch? ')
                rematch = rematch.upper()
                if rematch == 'YES':
                    finished = False
                    #resests stats after reset
                    stats['WINS'] = stats['LOSSES'] = stats['TIES'] = 0

            if game == 100:
                print('\n I am getting bored of beating you now! \n')

        elif player_selection == 'HELP':
            print(explain_rules())

        elif player_selection == 'EXIT':
            print('\nPathetic! You do not possess the strength to beat me!')
            finished = True

        else:
            print('Invalid input if you need help or wish to leave type help or exit')
introduction()
