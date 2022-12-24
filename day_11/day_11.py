from ast import literal_eval

class monkey:
    def __init__(self, 
            items = [], 
            operation = None, 
            test_value = None, 
            true_monkey = None, 
            false_monkey = None):
        self.items = items
        self.operation = operation,
        self.test_value = test_value
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspected = 0

    def test(self, index):
        if self.items[index]%self.test_value==0:
            self.throw(index, self.true_monkey)
        else:
            self.throw(index, self.false_monkey)

    def throw(self, index, to_monkey):
        to_monkey.catch(self.items[index])        

    def catch(self, item):
        self.items.append(item)
    
    def inspect(self, index):
        self.inspected+=1
        old = self.items[index]
        if '+' in self.operation:
            try:
                new = old + int(self.operation.split(' ')[-1])
            except:
                new = old + old
        elif '*' in self.operation:
            try:
                new = old * int(self.operation.split(' ')[-1])
            except:
                new = old * old
        # self.items[index] = new//3
        self.items[index] = new

    def play(self):
        for i, item in enumerate(self.items):
            self.inspect(i)
            self.test(i)
        self.items = []

monkeys = [monkey() for i in range(8)]
with open('input.txt', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        if "Monkey" in line:
            monkey_index = int(line.split(' ')[1].split(':')[0])
            current_monkey = monkeys[monkey_index]
        elif "items" in line:
            new_items = [int(item) for item in line.split(': ')[1].split(',')]
            current_monkey.items = new_items
        elif "Operation" in line:
            current_monkey.operation = line.split(': ')[1].split('=')[-1]
        elif "Test" in line:
            current_monkey.test_value = int(line.split(' ')[-1])
        elif "true" in line:
            current_monkey.true_monkey = monkeys[int(line.split(' ')[-1])]
        elif "false" in line:
            current_monkey.false_monkey = monkeys[int(line.split(' ')[-1])]

### part 1
for i in range(20):
    for m in monkeys:
        m.play()

inspections = sorted([m.inspected for m in monkeys])
print("monkey business part 1: ", inspections[-1]*inspections[-2])

### part 2
ggt = 1
for m in monkeys:
    ggt*=m.test_value

for i in range(10000):
    for m in monkeys:
        for i,item in enumerate(m.items):
            m.items[i] = item%ggt
        m.play()


inspections = sorted([m.inspected for m in monkeys])
print("monkey business part 2: ",inspections[-1]*inspections[-2])