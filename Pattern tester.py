repetition_length = 3
repetition = 0
counter_play = {'ROCK': 'PAPER', 'PAPER':'SCISSORS', 'SCISSORS':'ROCK'}
#while repetition_length > 0:
history = ['PAPER', 'ROCK','SCISSORS','PAPER', 'ROCK', 'ROCK'] 
recent_history = []
recent = range(1,7)
for games in recent: #Stores last 6 moves in recent history
    recent_history.append(history[-games])   
print(recent_history)
while repetition_length > 0:
    for games in range(1, 4): 
        if recent_history[games] == recent_history[games-repetition_length]:
            repetition += 1
            print('Repetition spotted in lengths ' + str(repetition_length)+ str(games))
    if repetition == 3:
        move = counter_play[history[-repetition_length]]
        print('I predict: ' + history[-repetition_length])
        repetition_length = 0
    else:
        repetition = 0
        repetition_length -= 1
        print('No pattern')
        if repetition_length == 0:
            move = 'None'
print(move)    