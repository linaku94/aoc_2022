def value(item):
    return ord(item)-96 if item.islower() else ord(item)-38

items = []
double_items = []
triple_items = []

with open('input.txt', 'r') as file:
    for k, line in enumerate(file.readlines()):
        if (k>0) & (k%3==0):
            item = items[0].intersection(*items[1:])
            triple_items.append(item.pop())
            items = []
        line = line.rstrip()
        item = set([i for i in line[:len(line)//2]]).intersection(set([i for i in line[len(line)//2:]]))
        double_items.append(item.pop())
        items.append(set([i for i in line]))

item = items[0].intersection(items[1],items[2])
triple_items.append(item.pop())

print(f'part one: {sum([value(item) for item in double_items])}')
print(f'part two: {sum([value(item) for item in triple_items])}')