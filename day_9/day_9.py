import numpy as np  
from copy import deepcopy

directions = {'R' : [1,0], 'L': [-1,0], 'U': [0,1], 'D' : [0,-1]}

def process_command(direction, steps, posH, posT, visited_positions, positions_T = []):
    for step in range(steps):
        posH = posH + direction
        posT = process_position(posH, posT)
        positions_T.append(tuple(posT))
    return posT, posH, positions_T
    
def process_position(posH, posT):
    dist = posH-posT
    if np.sqrt((dist**2).sum()) > 1.5:
        a = dist/np.sqrt((dist**2).sum())
        movement = np.sign(a) * np.ceil(np.abs(a))
        movement = movement.astype(int)
        posT += movement
    return posT

posH = np.array([0,0])
posT = np.array([0,0])
positions_T = [(0,0)]
with open('input.txt', 'r') as file:
    for line in file.readlines():
        direction, steps = line.strip().split()
        direction, steps = np.array(directions[direction]), int(steps)
        posT, posH, positions_T = process_command(direction, steps, posH, posT, positions_T)

print(f'number of visited positions: {len(set(positions_T))}')

rope_length = 9
for i in range(rope_length-1):
    posH = posT = np.array([0,0])
    positions_new = [(0,0)]
    for i, posH in enumerate(positions_T):
        posT = process_position(np.array(posH), posT)
        positions_new.append(tuple(posT))
    positions_T = deepcopy(positions_new)

print(f'number of visited positions of Tail {rope_length}: {len(set(positions_new))}')