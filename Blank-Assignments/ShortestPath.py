"""
This assignment is rather open-ended. You simply need to define a function that
can read the graph definitions defined in the tests below and output the path 
of the minimum distance between a start_node and end_node. You may use whatever 
data structures you think are helpful, but you should solve this function using
Dijkstra's Algorithm: http://www.geeksforgeeks.org/greedy-algorithms-set-6-dijkstras-shortest-path-algorithm/ .
"""
def shortest_path(start_node, end_node, graph):
  pass

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


for test in [small_test, medium_test, complex_test]:
  test()
  print "Woo! {} passes!\n".format(test.__name__)
