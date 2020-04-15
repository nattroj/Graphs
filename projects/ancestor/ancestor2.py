import sys, os
sys.path.append(os.path.join('..', 'graph'))

from graph import Graph
from util import Queue

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    # convert matrix to graph class structure to make lookups = O(n)
    for node in ancestors:
        parent, child = node

        # add parent and child vertex if they don't exist yet
        if not graph.has_vertex(parent):
            graph.add_vertex(parent)

        if not graph.has_vertex(child):
            graph.add_vertex(child)
        
        # add the relationship from child to parent
        graph.add_edge(child, parent)

    earliest_ancestors = []

    child = starting_node
    parents = graph.get_neighbors(child)

    if not len(parents):
        return -1
    
    queue = Queue()
    queue.enqueue((parents, child, 0))

    while queue.size():
        parents, child, traversed_distance = queue.dequeue()

        if not len(parents):
            earliest_ancestors.append((traversed_distance + 1, child))

        for parent in parents: 
            queue.enqueue((graph.get_neighbors(parent), parent, traversed_distance + 1))
    
    distances = list(map(lambda x: x[0], earliest_ancestors))
    furthest_distance = max(distances)

    earliest_ancestors = list(filter(lambda x: x[0] == furthest_distance, earliest_ancestors))
    earliest_ancestors = list(map(lambda x: x[1], earliest_ancestors))
    result = min(earliest_ancestors)

    return result