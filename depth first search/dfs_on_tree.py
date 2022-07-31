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
    if node is null:
        return

    if node.val > max_val:
        max_val = node.val

    # recursively
    dfs(node.left)
    dfs(node.right)


def get_max_val(root):
    dfs(root) #kick off the dfs from the root node 
    return max_val # since we dont need to return anything from dfs function it already changes glboal variable
