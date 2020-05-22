# import sys
# sys.path.append('../doubly_linked_list')
# from doubly_linked_list import DoublyLinkedList, ListNode

import sys
# print(sys.path)
print(type(sys.path))

sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?

   ['a', 'b', 'c', 'd']
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()
    
    def __len__(self):
        # return self.storage.length
        return self.size

        # or iterate across the list and count as we go
        
    # insert
    def enqueue(self, value): 
        self.storage.add_to_tail(value)
        self.size += 1

    # remove
    def dequeue(self): #remove
        if self.size == 0:
            return None

        remove_value =  self.storage.remove_from_head()

        self.size -= 1

        return remove_value
