def rps(p1, p2):
    d = {
        "scissors": "rock",
        "rock": "paper",
        "paper": "scissors"
    }

    if p1 == p2:
        return "Draw!"
    
    if d[p1] == p2:
        return "Player 2 won!"
    else:
        return "Player 1 won!"

        
    

print (rps('rock', 'scissors'))