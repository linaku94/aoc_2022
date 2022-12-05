
redundant_pairs = 0
overlapping_pairs = 0
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.rstrip()
        a, b = line.split(',')
        a, b = a.split('-'), b.split('-')
        A = set([i for i in range(int(a[0]), int(a[1])+1)])
        B = set([i for i in range(int(b[0]), int(b[1])+1)])
        if A<=B or B<=A:
            redundant_pairs+=1
        if len(A.intersection(B))!=0:
            overlapping_pairs+=1

print(f'redundant paris: {redundant_pairs}')  
print(f'overlapping paris: {overlapping_pairs}')      