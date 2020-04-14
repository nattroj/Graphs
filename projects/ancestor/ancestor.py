def get_parents(ancestors, child):
    parents = []

    for node in ancestors:
        if node[1] == child:
            parents.append(node[0])
    
    return parents

def earliest_ancestor(ancestors, starting_node, path=None):
    def recurse(ancestors, starting_node, path=None, early_ancestors=None):
        parents = get_parents(ancestors, starting_node)

        if path is None:
            path = []
        
        if not len(parents) and not len(path):
            return False
        
        new_path = [*path, starting_node]

        if not len(parents):
            return (len(new_path), new_path[-1])

        for parent in parents:
            ea = recurse(ancestors, parent, new_path, early_ancestors=early_ancestors)

            if ea is not None:
                early_ancestors.append(ea)

    early_ancestors = []

    if recurse(ancestors, starting_node, early_ancestors=early_ancestors) is False:
        return -1
        
    paths = map(lambda ancestor: ancestor[0], early_ancestors)
    longest_path = max(paths)

    earliest_ancestors = filter(lambda ancestor: ancestor[0] == longest_path, early_ancestors)

    return min(map(lambda ancestor: ancestor[1], earliest_ancestors))