
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # wrap the given value in a ListNode
        new_node = ListNode(value, None, None)
        self.length += 1
        # handle if list has a head
        
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # handle if list has no head
        else:
            self.head = new_node
            self.tail = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    #3
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    #1
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
    
        # there is a tail
        if self.tail:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node        
    
        # there is no tail(list)
        else:
            self.tail = new_node
            self.head = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        value = self.tail.value

        # this works too
        # self.delete(self.tail)
        
        # if 0 nodes
        if not self.tail:
            return

        # if head and tail are the same(1 node)
        elif self.head == self.tail:
           self.head = None
           self.tail = None

        # if more than 1 node
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.length -= 1

        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        # 1 way
        # self.delete(node)
        # node.next = self.head
        # self.head.prev = node
        # self.head = node

        #2nd way
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    #2
    def delete(self, node):

        self.length -= 1

        # if list is empty
        if not self.head and not self.tail:
            print("you got nothing on me!")
            return

        # if list has just one node is head
        elif self.head == self.tail:
             self.head = None
             self.tail = None

        # we have at least two node, and the node we want to delete is the head
        elif node == self.head:
             self.head = node.next
             self.head.prev = None
            # node.delete()

        # we have at lest two nodes, and the node we want to delete is the tail
        elif node == self.tail:
             self.tail = node.prev
             self.tail.next = None
            # node.delete()

        else:
             node.delete() # not calling delete


    """Returns the highest value currently in the list"""
    def get_max(self):
        highest_value = self.head.value
        current_node = self.head
        
        while current_node is not None:
            if current_node.value > highest_value:
                highest_value = current_node.value
            
            current_node = current_node.next

        return highest_value
