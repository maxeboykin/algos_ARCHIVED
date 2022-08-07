# think like a node within a tree instead of looking at the whole tree
# when you are a node the only thing you know are your value and how to get to your children

# so the basics would be this

def dfs(node, state):
    if node is None:
        return
    left = dfs(node.left, state)
    right = dfs(node.right, state)
return
# something to think about is what are we returning the value of from
# in terms of passing a value up from child to parent
# sometimes we want to return teh depth, sometimes the node or a null value if no node

# sometimes we want to pass down a state to your children like in examples when we need to know 
# if the current nodes value is larger than its parent 

# say we want to find the largest value in a binary tree 
# there are two ways we can address it 
# using the return value (divide and conquer or using a global variable)

# divid and conquer
# this is going all the way down to the leaves and nulls and slowly getting the max's 
# as you are recursively going back up the stack
# similar to merge sort 

def dfs(node):
    if node is null:
        return MIN_VALUE

    left_max_val = dfs(node.left)
    right_max_val = dfs(node.right)
    return max(node.val, left_max_val, right_max_val)


# seconds approach here is to use a global variable
# use global variable to record current max value 
# initialize to minimum value possible so any node will be large 

max_val = MIN_VALUE

def dfs(node):
    if node is None:
        return

    if node.val > max_val:
        max_val = node.val

    # recursively
    dfs(node.left)
    dfs(node.right)


def get_max_val(root):
    dfs(root) #kick off the dfs from the root node 
    return max_val # since we dont need to return anything from dfs function it already changes glboal variable


# find the max depth of the tree 
# when you get this problem do the divide and conquer method!! 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_max_depth(root: Node) -> int:
    def dfs(root):
        if not root:
            return 0

        return max(dfs(root.left), dfs(root.right)) + 1


# visible tree node or number of visible nodes
# return an int on how many nodes can be seen 
# i dont think we can create a global variable since its all subjective 
# based on where you are in the tree 
# my answer is below : not 100% sure it works but its close 

def visible_nodes(root: Node) -> int:
    def dfs(root, curHeight, count):
        if not root:
            return 0
        if root.val > curHeight:
            count = count + 1
        dfs(root.left, max(root.val, curHeight), count)
        dfs(root.right, max(root.val, curHeight), count)

        return count
    return dfs(root, -float('inf'), 0)


# answer from algo monster
def visible_tree_node(root: Node) -> int:
    def dfs(root, max_soFar):
        if not root:
            return 0

        total = 0

        if root.val >= max_soFar:
            total += 1 

        total += dfs(root.left, max(max_soFar, root.val))
        total += dfs(root.right, max(max_soFar, root.val))

        return total
    return dfs(root, -float('inf'))


# balanced binary tree 
# a balanced binary tree is defined as a trree such that either it is empty tree
# or both its subtree are balanced and has a height difference of at most 1 
# my answer below is WRONG

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_height(tree):
    if tree is None:
        return 0 
    left_height = tree_height(tree.left)
    right_height = tree_height(tree.right)
    if left_height == -1 or right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1

    return max(left_height, right_height) + 1 

def is_balanced(tree: Node) -> bool:
    return tree_height(tree) != -1






#def is_balancedWRONG(tree: Node) -> bool:
 #   def dfs(tree):
  #      if not tree:
   #         return 0
#
 #       left_tree = dfs(tree.left) + 1
  #      right_tree = dfs(tree.right) + 1
#
   #     return (abs(left_tree - right_tree) < 2)
