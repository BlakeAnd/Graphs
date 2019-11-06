from util import Stack, Queue
from graph import Graph  # These may come in handy

def earliest_ancestor(ancestors, starting_node):
    print("ancestors:", ancestors)
    print("ancestors 0 0:", ancestors[0][0])
    print("starting_node:", starting_node)
    graph = Graph()


    
    for edge in ancestors:
      graph.add_vertex(edge[0])
      graph.add_vertex(edge[1])

    for edge in ancestors:
      graph.add_edge(edge[1], edge[0])

    q = Queue()
    q.enqueue(starting_node)
    # paths = [[1,3,4], [1,3,7]]
    paths = [[starting_node]]


    while q.size() > 0:
      current = q.dequeue()
      
      
      print("curr", current)
      # print(graph.vertices[1])
      curr_path = paths[-1]
      for neighbor in graph.vertices[current]:
        print("neighbor", neighbor)
        print("cat arr", paths[-1] + [neighbor])
        paths.append(curr_path + [neighbor])
        print("paths:", paths)
        q.enqueue(neighbor)
      
      longest_path = paths[0]
      for path in paths:
        if len(path) > len(longest_path) or path[-1] < longest_path[-1]:
          longest_path = path

    print("return len:", len(longest_path))
    print("return:", longest_path[-1])
    if len(longest_path) <= 1:
      return -1
    else:
      return longest_path[-1]
    print("graph:", graph.vertices)
    

    