

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

 # applications of BSTS 
 # BSTs are used to look up existence of certain objects. insertion is much lowerer than 
 # sorted lists and its good for dynamic insertion 
 # howevcer most lanauges use hash tables, which is another way of looking up the existence 
 # of an object in a ocllection
 # most implementations are dynamically sized which can cause the lookup and insertion of items to 
 # approach O(1), so usually hash tables are preferred to BST 

 # hash tables are unsorted while BSTs are. if you want to maintain a sorted order
 # use BST 
 # its easy to look up the first element in the bST that is greater or smaller than a lookup 
 # value than a hash table 
 # its easy to find the k-th largest, smallest element 
 # dynamic hash tables usually have a lot of unused memory in order to make the 
 # insertion or deletion time approach O(1), where as BST uses all the memory
 # the user requested 

# determine if the tree is a valid BST 
class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    def dfs(root, min_val, max_val):
        if not root:
            return True
        if root.val < min_val or root.val > max_val:
            return False
        else:
            return dfs(root.left, min_val, root.value) and dfs(root.right, root.value, max_val)
    return dfs(root, -inf, inf) 


# the time complexity will be O(n) since there are n nodes and n - 1 edges so its O(2n-1) 
# which is O(n)

# insert into a binary tree 
# given a root node of a valid BST and a value to insert into the tree, return a new root node 
# with the value isnerseted 
def insert_bst(bst:Node, val: int) -> Node:
    def dfs(bst, val):
        if bst is None:
            return Node(val) #really important. at first i said return bst but 
        #this is where you insert the node each time!! 
        elif bst.val > val:
            return dfs(bst.left, val)
        elif bst.val < val:
            return dfs(bst.right, val)
        return bfs
    return dfs(root, value)


#invert a binary tree!!
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# my answer is below 
def invert_binary_tree(tree: Node) -> Node:
    def dfs(tree):
        if tree is None:
            return None
        tree_left = dfs(tree.left)
        tree_right = dfs(tree.right)
        tree.left = tree_right
        tree.right = tree_left
        return tree 

# solutions answer 
def invert_binary_tree(tree: Node) -> Node:
    def dfs(tree):
        if tree is None:
            return None
        return Node(tree.val, dfs(tree.right), dfs(tree.left))
    return dfs(tree)






