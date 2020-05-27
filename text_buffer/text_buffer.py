# file I/O - for another day

# add to the back of a text buffer
# add to the front of a text buffer
# delete to teh back of a text buffer
# delete to the from of a text buffer

# join text buffers together

# add to the middle

# Hey hello how are you today 

# array vs DLL
# array: add to back. O(1)
# array: add to front: O(n)

# array: delete from back: O(1)
# array: delete from front: O(n)

# array: join text buffers together: O(n)

# DLL: add to back: O(1)
# Dll: add to front: O(1)
# Dll: delete from front: O(1)
# Dll: delete from front: O(1)
# DLL: join text buffers together: O(1)

# __str___, to print out what's inside
# array, O(n)
# Dll, O(n)

# https://youtu.be/HadqhsdHZBE?t=5514

import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList, ListNode

class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()

    # return entire string and print
    def __str__(self):
        string_to_return = ""

        node = self.storage.head
        while node is not None:
            string_to_return += node.value
            node = node.next

        return string_to_return

    def join(self, other_buffer):
        # link tail of this buffer to the head of the other_buffer
        self.storage.tail.next = other_buffer.storage.head
        other_buffer.storage.head.prev = self.storage.tail
        
        # point our tail to the new tail
        self.storage.tail = other_buffer.storage.tail

    def append(self, string_to_add):
        # each character is a node        
        for char in string_to_add:
            self.storage.add_to_tail(char)

    def prepend(self, string_to_add):
        for char in string_to_add:
            self.storage.add_to_head(char)

    def delete_from_front(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_head()

    def delete_from_back(self, number_of_chars_to_remove):
        for _ in range(number_of_chars_to_remove):
            self.storage.remove_from_head()

    def find_text(self, text_to_find):
        pass


"hi how are you fine thank you"

text = TextBuffer()
text.append('hello')

other_buffer = TextBuffer()
other_buffer.append(' how are you')

text.join(other_buffer)

print(text)

