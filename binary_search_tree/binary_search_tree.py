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
from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.checked = False
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
    def for_each(self,fn):

        fn(self.value)

        if self.right:
            self.right.for_each(fn)

        if self.left:
            self.left.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        
        root = self
        order_stack = Stack()
        
        cur_nd = root
        if root.left is not None:
            while cur_nd.checked == False and root.left.checked==False:
                if cur_nd.left is not None and cur_nd.left.checked==False:
                    cur_nd = cur_nd.left
                
                else:
                    order_stack.push(cur_nd.value)
                    
                    order_stack.pop()
                    if cur_nd.right is not None:
                        cur_nd.right.in_order_print()
                    
                cur_nd.checked = True
                cur_nd = root
        order_stack.push(root.value)
        
        order_stack.pop()
        root.checked = True
        if root.right is not None:
            root = root.right
            root.in_order_print()
        
    
    
    def in_order_dft(self):
        pass
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        cur_nd = self
        N_queue = Queue()
        if cur_nd.checked == False:
            N_queue.enqueue(cur_nd.value)
            cur_nd.checked = True
        cur_l = cur_nd.left
        cur_r = cur_nd.right
        
        if cur_l is not None and cur_r is not None:
                N_queue.enqueue(cur_l.value)
                N_queue.enqueue(cur_r.value)
                
                cur_l.checked = True
                cur_r.checked = True
                cur_l.bft_print()
                                
        elif cur_r is not None:
                N_queue.enqueue(cur_r.value)
                
                cur_r.checked = True
                cur_r.bft_print()
        else:
                N_queue.enqueue(cur_l().value)
                cur_l.bft_print()
        while N_queue.size != 0:
                N_queue.dequeue
                
                
            
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        root = self
        D_stack = Stack()
        D_stack.push(root.value)
        root.checked = True
        D_stack.pop()
        cur_nd = root
        while cur_nd.left.checked == False and cur_nd.left is not None:
            cur_nd = cur_nd.left
            cur_nd.dft_print()
            cur_nd = root
        while cur_nd.right.checked == False and cur_nd.right is not None:
            cur_nd = cur_nd.right
            cur_nd.dft_print()
            cur_nd = root
            
        
        

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
