# trying to reinfoce the idea of states 
# given a ternary tree node ( each node has at most 3 children) find all root to leaf paths

class Node:
    def __init__(self, val, children=None) -> None:
        if children is None:
            children = []
        self.val = val
        self.children = children 

    
# looking to go through a tree and return an array like this
# [
#   1->2->3,
#   1->4,
#   1->6
# ]

# we need to keep track of the current path and that is the state! 

def ternary_tree_paths(root):
    #dfs helper function
    def dfs(root, path, res):
        # exit condition when you reached a leaf node, append pathds to results
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return

        # dfs on each non-null child 
        for child in root.children:
            if child is not None:
                dfs(child, path +[str(root.val)], res)

    res = []
    if root: dfs(root, [], res)
    return res
    

# in the recursive call in the previous solutiion, we ccretea a new list each time we recurse with path + 
# [root.val]. this is not space efficient because creating a new list requires allocating new space in memory
# and copying over each element. a more efficient way is to use a single list path and push and pop following the 
# call stack . 


def ternary_tree_paths(root):
    #dfs helper function
    def dfs(root, path, res):
        # exit condition when you reached a leaf node, append pathds to results
        if all(c is None for c in root.children):
            res.append('->'.join(path) + '->' + str(root.val))
            return

        # dfs on each non-null child 
        for child in root.children:
            if child is not None:
                path.append(str(root.val))
                dfs(child, path, res)
                path.pop()

    res = []
    if root: dfs(root, [], res)
    return res
    







