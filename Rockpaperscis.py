import random

game_choices = ['rock', 'paper', 'scissors']


userScore = 0
compScore = 0

def rand_pick():
    return random.choice(game_choices)

    
def win_lose(user, opp):
    if user == opp:
        return None
    elif (user == 'rock' and opp == 'scissors') or (user == 'scissors' and opp == 'paper') or (user == 'paper' and opp == 'rock'):
        return True 
    else:
        return False

def score_tracker(result):
    global userScore, compScore
    if result == True:
        userScore += 1
    elif result == False:
        compScore += 1
    elif result == None:
        compScore += 0
    return userScore, compScore

def validate_input(user):
    
    if user == 'rock' or user == 'paper' or user == 'scissors':
        return True
    else:
        return False 
    
def main():
    global userScore, compScore
    
    for i in range(6):
        user = input('Pick Rock, Paper, Scissors: ').lower()
        if not validate_input(user):
            print('Invalid Input.')
            continue
        
        opp = rand_pick()
        result = win_lose(user,opp)

        print(f'Computer choice: {opp.capitalize()}')

        if result == True:
            print('User wins this round!')
        elif result == False:
            print('Computer wins this round')
        else:
            print('Tied!')

        score_tracker(result)

        print(f'User: {userScore} | Computer: {compScore}')
    
    print(f'Final Score | User: {userScore} | Computa: {compScore}')
    


main()        
        
