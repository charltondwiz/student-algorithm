import random


class Node:
    def __init__(self, init_name):
        self.visited = []
        self.name = init_name

    def add(self, node):
        self.visited.append(node)

    def __repr__(self):
        return self.name


A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')

def generate_score(lst1, lst2, node, current_node_visited):
    if node in current_node_visited:
        return -2

    lst3 = [value for value in lst1 if value in lst2]
    return len(lst3)

def update_visited(group):
    for i in group:
        for j in group:
            if i != j and j not in i.visited:
                i.visited.append(j)


def generate_group(nodes):
    new_nodes = []
    for i in nodes:
        current_node = nodes.pop()
        current_group = [current_node]
        visited = current_node.visited
        for x in range(2):
            current_max = -1
            node_to_add = None
            for node in nodes:
                score = generate_score(visited, node.visited, node, visited)
                if score == -2:
                    continue

                if score > current_max:
                    current_max = score
                    node_to_add = node
            current_group.append(node_to_add)
            nodes.remove(node_to_add)
            update_visited(current_group)
            visited = current_node.visited + node_to_add.visited
        print(current_group)
        for node in current_group:
            new_nodes.append(node)
    for new_node in new_nodes:
        nodes.append(new_node)






nodes = [A, B, C, D, E, F, G, H, I]
random.shuffle(nodes)
generate_group(nodes)
print('------------------------')
random.shuffle(nodes)
generate_group(nodes)
print('------------------------')
random.shuffle(nodes)
generate_group(nodes)
print('------------------------')
random.shuffle(nodes)
generate_group(nodes)
print('------------------------')
print(nodes)
