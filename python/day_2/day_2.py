score = 0
points = {'X' : 1, 'Y' : 2, 'Z': 3 , 'A' : 1, 'B' : 2, 'C' : 3}
beats = {'A' : 'Z', 'B' : 'X', 'C' : 'Y'}
with open('input.txt', 'r') as file:
    for line in file.readlines():
        p1, p2 = line[0], line[2]
        ### part 1
        # score += points[p2]
        # if points[p1] == points[p2]:
        #     score += 3
        # elif beats[p1] != p2:
        #     score += 6

        ## part 2
        if p2 == 'X':
            score += points[beats[p1]]
        elif p2 == 'Y':
            score += points[p1] + 3
        elif p2 == 'Z':
            score += 6-points[p1]-points[beats[p1]] + 6

print(f'final score: {score}')