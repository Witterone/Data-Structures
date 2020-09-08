"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
    
    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def set_next(self,new_next):
        self.next = new_next
        
    def set_prev(self,new_prev):
        self.prev = new_prev
    
    def set_value(self,new_value):
        self.value = new_value
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        nue_node = ListNode(value, prev=None, next=None)
        if not self.head:
            self.head = nue_node
            self.tail = nue_node
            self.length += 1
        elif not self.head.get_next():
           
            self.head.set_prev(nue_node)
            
            nue_node.set_next(self.head)
            self.head = nue_node
            self.length += 1
            
            
        else:
            self.head.set_prev(nue_node)
            nue_node.set_next(self.head)
            self.head = nue_node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return None
       
        if not self.head.get_next():
            
            head = self.head
            
            self.head = None
            
            self.tail = None
            self.length += -1
            return head.get_value()
        
        value = self.head.get_value()
        
        self.head = self.head.get_next()
        self.length += -1
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value, prev=None, next=None)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            
        elif not self.tail.get_prev():
            self.tail.set_next(new_node)
            
            new_node.set_prev(self.tail)
            self.tail = new_node
            self.length += 1
            
        else:
            self.tail.set_next(new_node)
            new_node.set_prev(self.tail)
            self.tail=new_node
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return None
       
        if not self.tail.get_prev():
            
            tail = self.tail
            
            self.head = None
            
            self.tail = None
            self.length += -1
            return tail.get_value()
        
        value = self.tail.get_value()
        
        self.tail = self.tail.get_prev()
        self.length += -1
        return value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if not self.head:
            return "Not Found"
        else:
            current = node
            
            before = current.get_prev()
            after = current.get_next()
            if before:
                before.set_next(after)
            if after:
                after.set_prev(before)
            
            self.head.set_prev(current)
        
            current.set_next(self.head)
            current.set_prev(None)
            self.head = current
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if not self.tail:
            return "Not Found"
        else:
            current = node
            
            before = current.get_prev()
            after = current.get_next()
            
            if before:
                before.set_next(after)
            if after:
                after.set_prev(before)
            
            self.tail.set_next(current)
        
            current.set_prev(self.tail)
            current.set_next(None)
            self.tail = current

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if not self.head:
            return "Not Found"
        else:
            current = node
            
            before = current.get_prev()
            after = current.get_next()
            
            if before:
                before.set_next(after)
            if after:
                after.set_prev(before)
            
            current.set_next(None)
            current.set_prev(None)
            current.set_value(None)
            if current==self.head:
                self.head = after
            if current == self.tail:
                self.tail = before
            self.length += -1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        
        if self.head == self.tail:
            max_value = self.head
       
        max_value = self.head.get_value()
        
        if self.head.get_next():
            current = self.head.get_next()
        else:
            return max_value
       
        while current!=None:
            
            if current.get_value() > max_value:
                
                max_value = current.get_value()
            
            current = current.get_next()
        return max_value