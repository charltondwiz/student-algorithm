import random


class Node:
    def __init__(self, init_name):
        self.visited = []
        self.name = init_name

    def add(self, node):
        self.visited.append(node)

    def __repr__(self):
        return self.name


class Output:
    def __init__(self):
        self.output = ""


# config
number_of_people_in_a_group = 7
number_of_groups = 15
number_of_rounds = 6
total_people = 105


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


def generate_group(nodes, output):
    new_nodes = []
    num_groups = 0
    for x in range(number_of_groups):
        current_node = nodes.pop()
        current_group = [current_node]
        visited = current_node.visited
        for x in range(number_of_people_in_a_group - 1):
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
        # print(current_group)
        output.output += str(current_group) + "\n"
        num_groups += len(current_group)
        for node in current_group:
            new_nodes.append(node)
    for new_node in new_nodes:
        nodes.append(new_node)

    output.output += "\n --------------------------------- \n"
    return num_groups


counter = 0
target = number_of_rounds * total_people

while counter != target:
    try:
        counter = 0
        nodes = []
        output = Output()

        for x in range(total_people):
            new_node = Node(str(x))
            nodes.append(new_node)
        random.shuffle(nodes)
        for x in range(number_of_rounds):
            random.shuffle(nodes)
            counter += generate_group(nodes, output)
        print(counter)
        print(output.output + " finished with " + str(number_of_rounds) + " rounds.")

    except:
        print(counter)
        pass


