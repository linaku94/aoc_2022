import numpy as np 

def find_visibles(forest):
    N = forest.shape[0]
    vis_trees = N*4-4
    for i in range(1, N-1):
        for j in range(1, N-1):
            tree = forest[i,j]
            if max(forest[:i,j]) < tree or max(forest[i+1:,j]) < tree:
                vis_trees+=1
            elif max(forest[i,:j]) < tree or max(forest[i, j+1:]) < tree:
                vis_trees+=1
    return vis_trees

def viewing_score(tree, forest):
    local_scores= [directional_score(tree, forest, direct) for direct in [(-1,0), (1,0), (0,1), (0,-1)]]
    return np.prod(np.array(local_scores))

def directional_score(tree, forest, direct):
    N = forest.shape[0]-1
    l, k = tree[0] + direct[0], tree[1] + direct[1]
    score = 1
    while l>0 and k>0 and l<N and k<N and (forest[tree]>forest[l,k]):
        score+=1
        l, k = l+direct[0], k+direct[1]
    return score


forest = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        for number in line.strip():
            forest.append(number)

N = int(np.sqrt(len(forest)))
forest = np.array(forest).reshape((N,N))
print(f'visible trees in forest: {find_visibles(forest)}')

max_score = 0
for i in range(1, N-1):
    for j in range(1, N-1):
        max_score = max(max_score, viewing_score((i,j), forest))
print(f'best viewing score: {max_score}')