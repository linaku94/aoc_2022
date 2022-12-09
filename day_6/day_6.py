with open('input.txt', 'r') as file:
    message = file.read().strip()

length = 14 # 4
for i in range(len(message)):
    match = set([message[i+s] for s in range(length)])
    if len(match) == 14:
        print(f'found start of sequence after {i+length} characters')
        break