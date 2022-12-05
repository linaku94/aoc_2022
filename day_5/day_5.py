
cargo_state = {i : '' for i in range(9)}
with open('input.txt', 'r') as file:
    lines = file.readlines()
    for line in lines[:8]:
        for i in range(9):
            cargo_state[i] = line[i*4+1].strip() + cargo_state[i] 
    for line in lines[10:]:
        line = line.split()
        number, start, end = int(line[1]), int(line[3])-1, int(line[5])-1
        ### remove last inversion for part 2
        cargo_state[start], cargo_state[end] = cargo_state[start][:-number], cargo_state[end] + cargo_state[start][-number:]#[::-1]
        

res = [cargo_state[i][-1] for i in range(9)]
print(''.join([cargo_state[i][-1] for i in range(9)]))