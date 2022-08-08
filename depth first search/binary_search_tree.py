

# a BST is a rooted binary tree with a value of each internal node being greater than all values
# in the respective node's left subtree and less than ones in its right
# subtree 

# primary purpose of a BST is to search like a binary search

# the time complexity of each search is O(h) is the height of the tree

# another advantage of using BST compared to sorted list is that unlike a sorted list, 
# BST does not require each item in the list to move down an index like an
# sorted list does 

# for insertion, we perfrorm a search for that item and if its an empty tree 
# replace that empty tree with the new node containing the inserted value 

# insertion time complexity is the same as searching O(h) the height of the tree 
# ideally h is proportional to the log of the size of the tree 

# deleting an eleement from a BST doest show up ooften in interview questions but its similar to finding an element 
# in the tree
# if the nodes right subtree is empty then you bring its left subtree to its current position
# and remove the node. otherwise delete the leftmost portion of the right subtree
# and put it in its current position 
# deletion method complexity of time is proportional to the height of the tree as well 
# since you have to find the node and then delete it 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find(tree, val):
    if tree is None:
        return False
    if tree.val == val:
        return True
    elif tree.val < val:
        return find(tree.right, val)
    else:
        return find(tree.left, val)

def insert(tree, val):
    if tree is None:
        return Node(val)
    if tree.val < val:
        tree.right = insert(tree.right, val)
    elif tree.val > val:
        tree.left = insert(tree.left, val)
    return tree 

# ideally speaking the time complexity of eahc operation is O(log(n))
# if we insert each item from an already sorted list into a binary tree, it is going 
# to form a linked list and the time complexity of each operation becomes 
# O(n)

#note this!
# if a balanced binary tree is a binary tree whose subtrees are also balanced and have a height 
# difference of at max 1, the height of a balanced binary tree is proportional 
# to the log of its size 
# if a BST is balanced the operation is always going to be O(log(n))

# another thing to note is a balanced binary tree could be self balancing! 
# this is called an AVL tree and uses tree rotation after insertion to re balance the tree 
# a self balancing trree has a height of O(logn)

