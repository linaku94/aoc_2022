from treelib import Tree

def sum_data(tree, node):
    if node.is_leaf():
        return node.data 
    else:
        return sum([sum_data(tree, child) for child in tree.children(node.identifier)])

file_tree = Tree()
file_tree.create_node('/', 0, data = 0)
with open('input.txt', 'r') as file:
    for i, line in enumerate(file.readlines()):
        l = line.rstrip().split()
        if l[0] == "$":
            if l[1] == 'cd':
                if l[2] == '/' or current_node == 0:
                    current_node = 0
                if l[2] != '..':
                    for child_node in file_tree.children(current_node):
                       if child_node.tag == l[2]:
                        current_node = child_node.identifier
                else:
                    current_node = file_tree.parent(current_node).identifier
        elif l[0] == 'dir':
                file_tree.create_node(l[1], i, parent = current_node, data = 0)

        else:
            file_tree.create_node(l[1], i, parent = current_node, data = int(l[0]))

# print(f"pretty treeeeeeee \n {file_tree}")

sums = {}
for i, node in enumerate(file_tree.all_nodes()):
    if not node.is_leaf():
        sum_dir = sum_data(file_tree, node)
        sums[node.identifier] = sum_dir

print(sum([s for s in sums.values() if s <= 100000]))

used_space = sum_data(file_tree, file_tree.get_node(0))
search_for_at_least = 30000000-(70000000-used_space)

total = used_space
for s in sums.values():
    if s >= search_for_at_least:
        total = min(total, s)
print(total)