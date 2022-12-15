import sys

## part 1
y=2000000
y_pos = []
distances = []
positions = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip().split(' ')
        sx = int(line[2].split('=')[-1][:-1])
        sy = int(line[3].split('=')[-1][:-1])
        bx = int(line[8].split('=')[-1][:-1])
        by = int(line[9].split('=')[-1])
        dist = sum([abs(sx-bx), abs(sy-by)])
        distances.append(dist)
        positions.append([sx, sy, bx, by])
        if abs(y-sy)<=dist:
            y_pos.append([sx-dist+abs(y-sy), sx+dist-abs(y-sy)])
y_pos.sort()
start, end = y_pos[0][0], y_pos[0][1]
for ranges in y_pos[1:]:
    s, e = ranges[0], ranges[1]
    start = min(start, s)
    end = max(end, e)
print(end-start)

### part 2
N = 4000000
for y in range(N):
    if y%10000 == 0:
        print(y)
    y_pos = []
    for i, pos in enumerate(positions):
        dist = distances[i]
        sx, sy, bx, by = pos[0], pos[1], pos[2], pos[3]
        y_pos.append([sx-dist+abs(y-sy), sx+dist-abs(y-sy)])
    y_pos.sort()
    start, end = y_pos[0][0], y_pos[0][1]
    for ranges in y_pos[1:]:
        s, e = ranges[0], ranges[1]
        if end<s-1 and end+1<N and end>0:
            print(f'found x position x = {end+1} for {y=}')
            print(f'score {(end+1)*N+y}')
            sys.exit()
        else:
            start = min(start, s)
            end = max(end, e)


