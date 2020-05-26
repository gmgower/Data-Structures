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


# my_node = ListNode(12)
# my_node.value = 12
# my_node.prev = None
# my_node.next = None

# my_node.insert_after(25)
# my_node.value 25
# my_node.prev = 12
# my_node.next ---> ListNode(25)

# my_node.insert_after(100)
# my_node.value 25
# my_node.prev = 12

# reference line 14 & 23
# new_node = ListNode(100, my_node, None)


my_node = ListNode(12)
my_node.insert_after(25)
my_node.insert_after(100)
my_node.next.insert_after(99)

def iterate_list(node):
    while node is not None:
        print(node.value)
        node = node.next

# iterate_list(my_node)
# my_node = ListNode(12)
# ||
# my_node.next = ListNode(100)
# ||
# ListNode(99)
# ||
# ListNode(25)

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

"""Notes
there's two operations since it's doubly
link for every operation we
usually need to update two pointers and
in this case we need the head to know
that it's previous pointer is the new
head, and we need the new head to know
that it's next pointer is the old head
thus they get linked together in the
chain
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):  # overrides a built-in python func and lets us call the length function that we use for arrays on our linked list. len(linkedlist) https://youtu.be/Fe-QUooDw-8?t=4234
        return self.length
    

    """Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        """ 
        # Wrap the given value in a ListNode
        # 1 new_node is going to be the new head.
        new_node = ListNode(value, None, None)
        # Increase the lenght += 1
        self.length += 1
        # handle if list has a head
        if self.head:
            #https://youtu.be/V_yOEWqFTAo?t=5790
            # 2 new_node its .next points to the head or whatever the head is right now null/old node.
            new_node.next = self.head
            # the self.head (the old head node) its .prev points to the new node 
            self.head.prev = new_node
            # make self.head (old node) point to new node our new head of the list
            self.head = new_node
        # handle if list has no head
        else:
            self.head = new_node
            self.tail = new_node

        # dll = DoublyLinkedList()
        # dll.head - -> None
        # dll.tail - -> None

        """

        # 1 Q. What do we need to add to head & what are we adding to head?
        #  A. We need a list node
        new_node = ListNode(value)
        # 5 Update our length increase the length
        self.length += 1
        # 2 Q. What are the two distinct possibilities that are relevant to our linked list?
        #  A. If there is a node or if there isn't a node. If there's nothing there it's still the      head   and the tail
        if not self.head and not self.tail:
              # 3 Q. What do we know about our new node?
              #  A. Its the first & only node & it's the head & tail.
            self.head = new_node
            self.tail = new_node
        else: # otherwise 
            # 4. Add to front (prepend)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        #12 return the value
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        
        """
        new_node = ListNode(value)
        self.length += 1
    
        # there is a tail
        if self.tail:
        self.tail.next = new_node
        new_node.prev = self.tail
        # self.tail = new_node
    
        # there is no tail(list)
        else:
        self.tail = new_node
        self.head = new_node
        
        """

        # 6 create a new node
        new_node = ListNode(value)
        # 7 updating the length
        self.length += 1
        # 8 If there's nothing it's still the head and the tail
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else: # otherwise 
            # 9 resvers
            new_node.prev = self.tail
            self.head.next = new_node
        self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        #13
        value = self.tail.value
        # if 0 nodes
        if not self.tail:
            return

        # self.delete(self.tail)
        # not working with delete()
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
        #14
        # if node is self.head:
        #     return
        # self.add_to_head(node.value)
        # self.delete(node)        
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        #15
        # if node is self.tail:
        #     return 
        # self.delete(node)
        # self.add_to_tail(node.value)
        value = node.value
        self.delete(node) 
        self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):        
        # if list is empty

        # self.length -= 1

        # if not self.head and not self.tail:
        #     print("you got nothing on me!")
        #     return     

        # # if list has just one node is head
        # elif self.head == self.tail:
        #      self.head = None
        #      self.tail = None
        
        # # we have at least two node, and the node we want to delete is the head
        # elif node == self.head:
        #      self.head = node.next
        #      self.head.prev = None
        #     # node.delete()
    
        # # we have at lest two nodes, and the node we want to delete is the tail
        # elif node == self.tail:
        #      self.tail = node.prev
        #      self.tail.next = None
        #     # node.delete()
    
        # else:
        #      node.delete() # not calling delete        

        """ 
        10
        Why do you want to do delete first? So we can use the del func.

        """

        
        # 11 Planning
        # TODO: Do we need error checking if node is not in list?
        # update length
        self.length -= 1
        # This is the only node 
        if self.head is self.tail:  # is - is for reference equality. two reference refer to the same object
            self.head = None
            self.tail = None
        # It's the head
        elif node is self.head:
            self.head = node.next
            node.delete()
        # It's the tail
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        # It's in the middle
        else:
            node.delete()
        

    """Returns the highest value currently in the list"""

    def get_max(self):
        """
        #16
        # How to get max
        # create max var
        current = self.head
        max = self.head.value
        # Loop through nodes
        while(current is not None):
        # compare value in node to max found
            if current.value > max:
                max = current.value
            current = current.next
        # return max found
        return max
        """

    # walk through the entire list
    # keep track of the biggest value we've found

        highest_value = self.head.value
        current_node = self.head
        
        while current_node is not None:
            if current_node.value > highest_value:
                highest_value = current_node.value
            
            current_node = current_node.next

        return highest_value

    # https://youtu.be/HadqhsdHZBE?t=2722
    def find_middle(self):
        # start with two pointers
        middle = self.head
        end = self.head

        while end.next != None and end.next.next !=None:
            # end = end.next.next
            # middle = middle.next
            end = end.next.next
            middle = middle.next

        return middle
    
    # head should now be the tail
    # tail should now be head
    # no recursion, no other data structure
    def reverse_list(self):
        pass

dll = DoublyLinkedList()
dll.add_to_tail(1)
dll.add_to_tail(2)
dll.add_to_tail(3)
dll.add_to_tail(4)
dll.add_to_tail(5)
# dll.add_to_tail(6)

middle = dll.find_middle()
print(middle.value)
