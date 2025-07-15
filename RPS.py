import random

my_history = []
opp_history = []

def player(prev_opponent_play):
    if prev_opponent_play != '':
        opp_history.append(prev_opponent_play)
    moves = ['R', 'P', 'S']
    beats = {'R': 'P', 'P': 'S', 'S': 'R'}
    loses_to = {v: k for k, v in beats.items()}

    # Start with random if no history
    if not my_history:
        move = random.choice(moves)
        my_history.append(move)
        return move

    # Detect if opponent copies last move:
    if len(opp_history) > 1:
        if opp_history[-1] == my_history[-1]:
            # Opponent copied you last round, so play what beats your last move
            move = beats[my_history[-1]]
            my_history.append(move)
            return move

    # Detect if opponent plays what beats your last move:
    if len(opp_history) > 1:
        if opp_history[-1] == beats[my_history[-1]]:
            # Opponent tries to beat your last move, so play what beats their last move
            move = beats[opp_history[-1]]
            my_history.append(move)
            return move

    # Check for losing streak (last 3 rounds)
    if len(my_history) >= 3:
        losses = 0
        for i in range(-3, 0):
            if opp_history[i] == beats[my_history[i]]:
                losses += 1
        if losses >= 2:
            # Losing streak, switch to random to confuse opponent
            move = random.choice(moves)
            my_history.append(move)
            return move

    # Frequency analysis of opponent moves:
    freq = {'R': 0, 'P': 0, 'S': 0}
    for m in opp_history[-10:]:  # last 10 moves only
        freq[m] += 1

    prediction = max(freq, key=freq.get)
    # With 10% chance, randomize to avoid being predictable
    if random.random() < 0.1:
        move = random.choice(moves)
    else:
        move = beats[prediction]

    my_history.append(move)
    return move
