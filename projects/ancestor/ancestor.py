def get_parents(ancestors, child):
    parents = []

    for node in ancestors:
        if node[1] == child:
            parents.append(node[0])
    
    return parents

def earliest_ancestor(ancestors, starting_node, path=None):
    parents = get_parents(ancestors, starting_node)

    if path is None:
        path = []
    
    if not len(parents) and not len(path):
        return -1
    
    new_path = [*path, starting_node]

    if not len(parents):
        return starting_node

    for parent in parents:
        ea = earliest_ancestor(ancestors, parent, new_path)

        if ea is not None:
            return ea