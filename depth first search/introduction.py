
#below is a classis recursion example
def factorial(n):
    if n <= 1: # base case 
        return 1
    return n* factorial(n-1) # recursive call


print(factorial(3))

# the tree data structure is very important
# the root node at the top is at level 0 
# the children of root node are said to have a depth of 1 and a height of #max levels -1
# the nodes at the bottom of the tree are the leaves and have a height of 0 and a depth of their level 

# a binary tree or a n-ary tree is in which eacn node has no more than n children 
# so a binary tree, each node has to have between 0 to 2 children

class Node:
    def __init__(self, val):
        self.val = val
        self.left = none
        self.right = none

# in javascript
class Node {
    constructor(val, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

# a balanced binary tree fulfills the condition of the height difference on the left and right subtree of the node 
# is not more than 1 
# searching, insertion and deletion takes O(log n) instead of O(n) in an unbalanced bianry tree 

# Tree Traversals! 

#in-order traversal visits the left branch first, then the current node and finally the right branch 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(root: Node):
    if root is not None:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)

def pre_order_traversal(root: Node):
    if root is not None:
        print(root.val)
        in_order_traversal(root.left)
        in_order_traversal(root.right)

def post_order_traversal(root: Node):
    if root is not None:
        in_order_traversal(root.left)
        in_order_traversal(root.right)
        print(root.val)



# depth first search is a bold search, go deep as we can to look for a value 
# and if there is noting new to discover we retrace our steps to find something new 
# the pre order traversal of a tree is a depth first search 

function dfs(root, target) {
        if (!root) return null;
        if (root.val === target) return root;

        left = dfs(root.left)
        if (left != null) return left
        right = dfs(root.right)
        # we would only get here if the entire sub left tree is null and no target is found
        # so here we will just search the right side and return right no matter what
        # if right finds the target it will be returned
        # if we hit the bottom and its null we return null which is also the value of right
        return right;
        }







