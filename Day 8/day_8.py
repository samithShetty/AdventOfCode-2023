### Part 1
# with open('input.txt', 'r') as infile:
#     network = dict()
#     lines = infile.readlines()
#     moves = [c=="R" for c in lines[0].strip()]
#     for line in lines[2:]:
#         network[line[:3]] = (line[7:10], line[12:15])
#     count = 0
#     current_node = 'AAA'
#     while current_node != 'ZZZ':
#         current_node = network[current_node][moves[count%len(moves)]]
#         count += 1
#     print(count)

### Part 2
from math import lcm
with open('input.txt', 'r') as infile:
    network = dict()
    lines = infile.readlines()
    moves = [c=="R" for c in lines[0].strip()]
    for line in lines[2:]:
        network[line[:3]] = (line[7:10], line[12:15])

    start_nodes = [node for node in network.keys() if node.endswith('A')]
    end_nodes = [node for node in network.keys() if node.endswith('Z')]
    counts = []
    
    for node in start_nodes:
        count = 0
        while node not in end_nodes:
            node = network[node][moves[count%len(moves)]]
            count += 1
        counts.append(count)
    print(lcm(*counts))
        