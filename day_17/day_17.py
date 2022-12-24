
class Tetris:
    def __init__(self, name, rocks):
        
        height = max(rocks, key = lambda x:x[1])[1]+4
        if name == '-':
            self.coords = [[i, height] for i in range(2,6)]
        elif name == '+':
            self.coords = [[i, height+1] for i in range(2,5)]
            self.coords.extend([[3,height], [3, height+2]])
        elif name == 'L':
            self.coords = [[i, height] for i in range(2,5)]
            self.coords.extend([[4, height+1], [4, height+2]])
        elif name == 'I':
            self.coords = [[2, height+i] for i in range(4)]
        elif name == 'O':
            self.coords = [[2, height], [3, height], [2, height+1], [3, height+1]] 
        self.status = 'falling'
        self.rocks = rocks
        self.height = height

    def fall(self):
        if self.status == 'stopped':
            # print('can\'t fall further')
            return None
        new_coords = []
        for i, c in enumerate(self.coords):
            new_coords.append([c[0], c[1]-1])
            if [c[0], c[1]-1] in self.rocks:
                self.status = 'stopped'
                # print('stop falling')
                return None
        self.coords = new_coords

    def apply_jet(self, jet):
        new_coords = []
        if jet == '>':
            for c in self.coords:
                new_coords.append([c[0]+1, c[1]])
                if c[0]+1>=7 or [c[0]+1, c[1]] in self.rocks:
                    return None
            self.coords = new_coords
        elif jet == '<':
            for c in self.coords:
                new_coords.append([c[0]-1, c[1]])
                if c[0]-1<0 or ([c[0]-1, c[1]]) in self.rocks:
                    return None
            self.coords = new_coords


    def append_to_rocks(self):
        for c in self.coords:
            self.rocks.append(c)
        for c in self.rocks:
            if c[1]<self.height-70:
                self.rocks.remove(c)
        return self.rocks



jets = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        for s in line:
            jets.append(s)

rocks = [[i, 0] for i in range(7)]
new_rocks = ['-', '+', 'L', 'I', 'O']
k = 0
print(len(jets))
# breakpoint()
for i in range(5*len(jets)*10):
    if i%len(jets) == 0:
        print(max(rocks, key = lambda x:x[1])[1])
    new_rock = Tetris(new_rocks[i%5], rocks)
    while new_rock.status == 'falling':
    # for k in range(4):
        # print(new_rock.coords)
        new_rock.apply_jet(jets[k%len(jets)])
        # print(jets[i%len(jets)])
        # print(new_rock.coords)
        new_rock.fall()
        k+=1
    
    rocks = new_rock.append_to_rocks()
    # print(rocks)
print(max(rocks, key = lambda x:x[1])[1])

import numpy as np  
test = np.zeros((7,new_rock.height))
for r in rocks:
    test[r[0], r[1]] = 1
import matplotlib.pyplot as plt 
plt.imshow(test[:,-100:].transpose(), origin = 'lower')
plt.show()