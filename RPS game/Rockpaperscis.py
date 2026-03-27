import random
from flask import Flask,render_template, request

app = Flask(__name__)
game_choices = ['rock', 'paper', 'scissors']
user_history = []

userScore = 0
compScore = 0

def rand_pick():
    return random.choice(game_choices)
def ai_pick():
    if not user_history:
        return random.choice(game_choices)
    freq_play = max(set(user_history), key =user_history.count)
    last_play = user_history[-1]

    def counter(play):
        if play == 'rock':
            return 'paper'
        elif play == 'paper':
            return 'scissors'
        else:
            return 'rock'
    
    strategy = random.random()

    if strategy < 0.5:
        return counter(freq_play)
    elif strategy < 0.8:
        return counter(last_play)
    else:
        return random.choice(game_choices)
    
def win_lose(user, opp):
    if user == opp:
        return 'Tied!'
    elif (user == 'rock' and opp == 'scissors') or (user == 'scissors' and opp == 'paper') or (user == 'paper' and opp == 'rock'):
        return 'User wins!' 
    else:
        return 'Computer wins!'

def score_tracker(result):
    global userScore, compScore
    if result == 'User wins!':
        userScore += 1
    elif result == 'Computer wins!':
        compScore += 1
    elif result == 'Tied!':
        compScore += 0
    return userScore, compScore


@app.route('/', methods = ['GET', 'POST'])  
def index():
    global userScore, compScore

    result = None
    opp = None
    if request.method == 'POST':
        user = request.form['choice']
        user_history.append(user)
        opp = ai_pick()

        result = win_lose(user,opp)

        score_tracker(result)

    return render_template(
        "index.html",
        opp = opp,
        result = result,
        compScore = compScore,
        userScore = userScore
    
    
    )
    
if __name__ == '__main__':
    app.run(debug=True)


        
    


       
        
