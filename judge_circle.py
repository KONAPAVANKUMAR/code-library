
def judge_circle(moves):
    dict_moves = {
        'U' : 0,
        'D' : 0,
        'R' : 0,
        'L' : 0
    }
    for char in moves:
        dict_moves[char] = dict_moves[char] + 1
    return dict_moves['L'] == dict_moves['R'] and dict_moves['U'] == dict_moves['D']
