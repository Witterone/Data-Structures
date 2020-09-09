"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        
        new_BSTN = BSTNode(value)
        cur_nd = self
        while cur_nd is not new_BSTN:
            
            if new_BSTN.value < cur_nd.value:
                if cur_nd.left is None:
                    cur_nd.left = new_BSTN
                    
               
                cur_nd = cur_nd.left
            else:
                if cur_nd.right is None:
                    cur_nd.right = new_BSTN
                
                cur_nd = cur_nd.right
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        cur_nd = self
        while cur_nd.value != target:
            if target< cur_nd.value:
                if cur_nd.left is not None:
                    cur_nd = cur_nd.left
                else:
                    return False
            else:
                if cur_nd.right is not None:
                    cur_nd = cur_nd.right
                else:
                    return False
                
        return True

    # Return the maximum value found in the tree
    def get_max(self):
        cur_nd = self
        max_val=self.value
        while cur_nd.right is not None:
            cur_nd = cur_nd.right
            if cur_nd.value > max_val:
                max_val = cur_nd.value
            
        return max_val

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        cur_nd = self
        root = self
        cur_nd.value = fn(cur_nd.value)
        while cur_nd.right is not None or cur_nd.left is not None:
            cur_r = cur_nd.right
            cur_l = cur_nd.left
            if cur_l is not None:
                cur_l.value = fn(cur_l.value)
            if cur_r is not None: 
                cur_r.value = fn(cur_r.value)
            if cur_l is not None:
                cur_nd = cur_l
            elif cur_r is not None:
                cur_nd = cur_r
                
            else:
                cur_nd = cur_nd
        
        if root.right is not None:
                cur_nd = root.right
        
        while cur_nd.right is not None or cur_nd.left is not None:
            cur_r = cur_nd.right
            cur_l = cur_nd.left
            if cur_l is not None:
                cur_l.value = fn(cur_l.value)
            if cur_r is not None: 
                cur_r.value = fn(cur_r.value)
            if cur_l is not None:
                cur_nd = cur_l
            elif cur_r is not None:
                cur_nd = cur_r
        
        
        
        
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass
    def in_order_dft(self):
        pass
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
