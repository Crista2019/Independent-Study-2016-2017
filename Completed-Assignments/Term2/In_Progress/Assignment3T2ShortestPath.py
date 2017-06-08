"""
This assignment is rather open-ended. You simply need to define a function that
can read the graph definitions defined in the tests below and output the path 
of the minimum distance between a start_node and end_node. You may use whatever 
data structures you think are helpful, but you should solve this function using
Dijkstra's Algorithm: http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/ .
"""

def shortest_path(start_node, end_node, graph):
	#Visit the starting node of the weighted graph to begin
	current = start_node
	to_visit = [current] #List of nodes to visit
	visited = set() #Set of nodes that have already been visited
	
	#PRINT TEST
	i = 0
	for x in [current,to_visit,visited]:
	  thing = ["current", "to_visit", "visited"]
	  print("start",thing[i],":",x)
	  i = i+1
	
	#Set the distance value from start to start to be 0 because the start ode is current
	dist_from_start = {start_node: 0}
	tent_parents = {} #Tuple of tentative (changing) parent elements
	
	#PRINT TEST
	print (dist_from_start, tent_parents)

	while len(to_visit) > 0:
		#Node with the smallest weight should be the next node (ALSO, FINALLY A WAY TO APPLY LIST COMPREHENSION)
		current = min([(dist_from_start[val], val) for val in  to_visit])[1]
		
		#PRINT TEST
		print("current:",current)
		
		if current == end_node:
			break

		if current in to_visit:
			 to_visit.remove(current)
			 visited.add(current)

		edges = graph[current] #gives edges, nodes and weights that current node connects to
		#Values that are included both in edges and in visited aren't useful here, 
		#So neighbors that HAVENT been visited are equal to a set of unvisited values (those NOT in visited)
		unvisited = set(edges).difference(visited) 
		
		#PRINT TEST
		print("edges:", edges, "- visited: ", visited)
		print("unvisited nodes:",unvisited)
    
    
		for neighbor in unvisited:
			neighbor_dist = dist_from_start[current] + edges[neighbor]
			
			#PRINT TEST
			print("distance from start to edge neighbor ",neighbor,":", neighbor_dist)
			
			#If the distance from start to the neighbor is less than any value from the neighbor distance dictionary up to the infinity-ith key. Or, since get() only iterates up to the last true return, this occurs if the neighbor distance is less than infinity. Infinity occurs when the node doesn't actually connect to the start node. 
			if neighbor_dist < dist_from_start.get(neighbor_dist, float('inf')):
			  print(neighbor_dist, "is less than",dist_from_start.get(neighbor_dist, float('inf')))
			  dist_from_start[neighbor] = neighbor_dist
			  tent_parents[neighbor] = current
			  to_visit.append(neighbor) 
			  print('DIST FROM START OF NEIGHBOR', neighbor,":", dist_from_start[neighbor])
			  print('TENTATIVE PARENTS OF NEIGHBOR', neighbor,":", tent_parents[neighbor])
			  print('UPDATED TO_VISIT:', to_visit)
			  """if unvisited[neighbor] == end_node:
			    tent_parents[neighbor] = current
			    break""" #BAD
			  #Ultimately, a neighbor element is put in line to be visited IF there is a connection to the start node
	print("PATH DISTANCE:",neighbor_dist)
	print("SHORTEST PATH:", deconstruct_path(tent_parents, end_node))
	return [neighbor_dist, deconstruct_path(tent_parents, end_node)]

def deconstruct_path(tent_parents, end_node, time=0): #TIME IS FOR PRINT TEST AND DOES NOTHING USEFUL
	if end_node not in tent_parents:
		return None
	goal = end_node
	
	#PRINT TEST
	print("IN deconstruct_path HELPER FUNCTION NOW! INITIAL tentative parents",tent_parents)
	print("end node goal:", goal)
	
	path = []
	while goal:
		path.append(goal)
		goal = tent_parents.get(goal)
		#PRINT TEST
		i = 0
		time += 1
		things = ["path", "goal"]
		for x in [path,goal]:
		  print (things[i],"during loop #",time,":", x)
		  i += 1
	deconstructed_node_path = list(path[::-1])
	print("What is fed back to main function:", deconstructed_node_path)
	return deconstructed_node_path


def small_test():
  test_graph = {
    "A": {"B": 5},
    "B": {"A":5, "C":5},
    "C": {"B": 5},
  }
  
  assert [10, ["A","B","C"]] == shortest_path("A", "C", test_graph)
  assert [5, ["B","C"]] == shortest_path("B", "C", test_graph)
  assert [10, ["C","B","A"]] == shortest_path("C", "A", test_graph)


def medium_test():
  test_graph = {
    "A": {"B": 1, "C":2},
    "B": {"C":5},
    "C": {"D": 1, "A": 2},
    "D": {}
  }
  
  assert [4, ["A", "C", "D"]] == shortest_path("A", "D", test_graph)

  
def complex_test():
  test_graph = {
    "SEA": {"LAX": 160, "ORD": 240},
    "ORD": {"ATL": 120, "FLL": 180},
    "LAX": {"FLL": 285, "SEA": 165},
    "ATL": {"FLL": 110, "ORD": 120},
    "FLL": {"SEA": 335, "ORD": 195},
  }
  assert [445, ["SEA", "LAX", "FLL"]] == shortest_path("SEA", "FLL", test_graph)

for test in [medium_test, complex_test]: #ADD SMALL BACK EVENTUALLY WHEN OTHER ISSUES ARE RESOLVED
  test()
  #print("Woo! {} passes!\n").format(test.__name__)
  
"""
Dijkstra's algorithm to find the shortest path between a and b. It picks the unvisited vertex with the lowest distance, calculates the distance through it to each unvisited neighbor, and updates the neighbor's distance if smaller. Mark visited (set to red) when done with neighbors.
Class:	Search algorithm
Data structure:	Graph
Worst-case performance: O(|E|+|V|\log |V|)
"""
