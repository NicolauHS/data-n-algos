# We start by building our graph structure with hash tables to indicate
# the relation between nodes
graph = {}

# This right here states that start is a node that connects to A and B
# and the path between start and a has weight 6, the path between start
# and B has weight 2
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5

graph["end"] = {}

# We now start modeling the costs hash map. In this structure, we are 
# going to store the total costs to travel to each node, changing them
# as we find faster routes.

# We start by filling just the basic information on each node's cost and
# assuming the cost to reach the end is infinite
infinite = float("inf")

costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinite

# Finally, we model the parents, this is the actual structure that is
# going to help us find the optimal path by relating the nodes in a 
# sequence that we use to create a route.
parents = {}
parents["a"] = "start"
parents["b"] = "start"

# As we don't yet know which route is best, we assume there is no 
# parent to the end node 
parents["end"] = None

processed = []

def find_lowest_cost_node(costs):
  lowest_cost = float("inf");
  lowest_cost_node = None

  for node in costs:
    cost = costs[node]
    if cost < lowest_cost and node not in processed:
      lowest_cost = cost
      lowest_cost_node = node
  
  return lowest_cost_node

def show_final_path(parents):
  current = "end"
  path = []

  while "start" not in current:
    parent = parents[current]
    path.append(current)
    current = parent

  path.append("start")
  
  print("Fastest path between start and end: \n")
  
  for i in reversed(path):
    if "end" not in i:
      print(f"{i} -> ", end='')
    else:
      print(f"{i}")

# Now, for a step-by-step of the algorithm:

# Finds the lowest cost node that was not processed
node = find_lowest_cost_node(costs)

# When there are no nodes left, the this loop will stop
while node is not None:
  cost = costs[node]
  neighbors = graph[node]
  # Iterate every neighbor of the current node
  for n in neighbors.keys():
    new_cost = cost + neighbors[n]
    # If reaching a neighbor through this node is faster
    if costs[n] > new_cost:
      # Change cost of travel for that neighbor
      costs[n] = new_cost
      # Also list this node as the new parent for the neighbor
      parents[n] = node
  
  processed.append(node) # Marks node as processed
  node = find_lowest_cost_node(costs) # Finds next node to process

show_final_path(parents)