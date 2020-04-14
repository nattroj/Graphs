def get_parents(ancestors, child):
    parents = []

    for node in ancestors:
        if node[1] == child:
            parents.append(node[0])
    
    return parents

def find_earliest_ancestors(ancestors, starting_node, path=None, earliest_ancestors=None):
    parents = get_parents(ancestors, starting_node)

    if path is None:
        path = []
    
    if earliest_ancestors is None:
        earliest_ancestors = []
    
    if not len(parents) and not len(path):
        return None
    
    new_path = [*path, starting_node]

    if not len(parents):
        ea = (len(new_path), new_path[-1])
        earliest_ancestors.append(ea)

    for parent in parents:
        find_earliest_ancestors(ancestors, parent, new_path, earliest_ancestors)
    
    return earliest_ancestors

def earliest_ancestor(ancestors, starting_node, path=None):

    earliest_ancestors = find_earliest_ancestors(ancestors, starting_node)

    if earliest_ancestors is None:
        return -1
        
    paths = map(lambda ancestor: ancestor[0], earliest_ancestors)
    longest_path = max(paths)

    earliest_ancestors = filter(lambda ancestor: ancestor[0] == longest_path, earliest_ancestors)

    results = map(lambda ancestor: ancestor[1], earliest_ancestors)

    return min(results)

# test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
# print(earliest_ancestor(test_ancestors, 10))