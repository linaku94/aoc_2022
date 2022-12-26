from structlinks.DataStructures import LinkedList
import numpy as np 

llist = LinkedList()
orderlist = []
with open('input.txt', 'r') as file:
    for line in file.readlines():
        new_node = int(line.strip())
        control = 0
        while (new_node, control) in llist:
            control+=1
        llist.append((new_node, control))
        orderlist.append((new_node, control))

## part 1
# for k, element in enumerate(orderlist):
#     index = llist.index(element)
#     llist.pop(index)
#     index_new = (index+element[0])%(len(llist))
#     llist.insert(index_new, element)

# indices = [1000, 2000, 3000]
# start_index = llist.index((0,0))
# print(f"decoder key part 1: {sum([llist[(start_index+ind)%len(llist)][0] for ind in indices])}")

## part 2
llist = llist.map(lambda x:(x[0]*811589153,x[1]))
orderlist = [(elem[0]*811589153, elem[1]) for elem in orderlist]
for i in range(10):
    print(i)
    for k, element in enumerate(orderlist):
        index = llist.index(element)
        llist.pop(index)
        index_new = (index+element[0])%(len(llist))
        llist.insert(index_new, element)

indices = [1000, 2000, 3000]
start_index = llist.index((0,0))
print(f"decoder key part 2: {sum([llist[(start_index+ind)%len(llist)][0] for ind in indices])}")
