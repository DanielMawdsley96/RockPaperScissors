import random

Win_List = [('ROCK', 'SCISSORS'),  # Rock beats Scissors
            ('SCISSORS', 'PAPER'),  # Scissors beats paper
            ('PAPER', 'ROCK')]  # Paper beats rock obvs  

selection_list = ['ROCK', 'PAPER', 'SCISSORS'] 

Stats = {'player':0, 'computer':0, 'ties':0}

def GameEnd():
    if Stats['player'] == 2:
        print('You have won! Well done!')
        return True
    elif Stats['computer'] == 2:
        print('You have lost! Better luck next time!')
        return True
    else:
        return False
            
def PlayGame():
    ready = input('Are you ready? (type YES to play) ')
    ready = ready.upper()
    if ready == 'YES':
        Finished = False
        while Finished == False:
            player_selection = input('Your selection is: {} '.format(selection_list)) #Player enters their move
            player_selection = player_selection.upper()
            
            if player_selection in selection_list:
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
                print("             Stats        "
                      "\n Player | Computer | Ties"
                      "\n    {player}        {computer}        {ties}"
                      "\n                    ".format(**Stats))
                Finished = GameEnd()
        
        
        
PlayGame()        
    
    
    
    


