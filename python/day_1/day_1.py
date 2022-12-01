
calories = [0]
with open('input.txt', 'r') as file:
    for line in file.readlines():
        if line == '\n':
            calories.append(0)
        else:
            calories[-1] += int(line.rstrip())

print(f'maximum number of calories: {max(calories)}')
calories.sort()
print(f'calories of top 3 elves: {sum(calories[-3:])}')