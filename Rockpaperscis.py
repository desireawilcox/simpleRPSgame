import random

game_choices = ['Rock', 'Paper', 'Scissors']



def rand_pick():
    opp_pick = random.choice(game_choices)
    return opp_pick

    
def win_lose(user, opp):
    if user == opp:
        return None
    elif (user == 'Rock' and opp == 'Scissors') or (user == 'Scissors' and opp == 'Paper') or (user == 'Paper' and opp == 'Rock'):
        return True
    else:
        return False 
    

user = input('Pick Rock, Paper, Scissors: ')
opp = rand_pick()
win_lose(user,opp)
print(f'Computer choice: {opp}')
if win_lose(user,opp):
    print('User wins this round!')
else:
    print('Computer wins this round')


    
    
