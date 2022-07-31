
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


