import numpy as np 
import matplotlib.pyplot as plt 

cc = 1
time_step = 1
check_cycles = [20+i*40 for i in range(6)]
score = 0
drawing = np.zeros((6,40))
with open('input.txt', 'r') as file:
    for i, line in enumerate(file.readlines()):
        if time_step in check_cycles:
            score += (time_step)*cc
        if (time_step-1)%40 in [cc-1, cc, cc+1]:
            drawing[(time_step-1)//40,(time_step-1)%40] = 1
        time_step+=1
        command = line.strip()
        if "addx" in command:
            increment = int(command.split(' ')[-1])
            if (time_step-1)%40 in [cc-1, cc, cc+1]:
                drawing[(time_step-1)//40,(time_step-1)%40] = 1
            if time_step in check_cycles:
                score += (time_step)*cc
            cc += increment
            time_step+=1

print(f"score first part: {score}")

plt.imshow(drawing, cmap = 'Greys')
plt.show()