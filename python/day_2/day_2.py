score = 0
points = {'X' : 1, 'Y' : 2, 'Z': 3 , 'A' : 1, 'B' : 2, 'C' : 3}
beats = {'A' : 'Z', 'B' : 'X', 'C' : 'Y'}
loses = {'A' : 'Y', 'B' : 'Z', 'C' : 'X'}
with open('input.txt', 'r') as file:
    for line in file.readlines():
        p1, p2 = line[0], line[2]
        # score += points[p2]
        # if points[p1] == points[p2]:
        #     score += 3
        # elif beats[p1] != p2:
        #     score += 6
        if p2 == 'X':
            score += points[beats[p1]]
        elif p2 == 'Y':
            score += points[p1] + 3
        elif p2 == 'Z':
            score += points[loses[p1]] + 6

print(f'final score: {score}')