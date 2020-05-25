import sys

sys.path.append('../doubly_linked_list')

from doubly_linked_list import DoublyLinkedList

class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.



    node(h) -- node(g) -- node(d)
    ----------------------------
    | a b c d e f g             |


    dict
    {h: val} # guaranted to keeps stuff in order
    """
    
    def __init__(self, limit=10):
        
    # Keeps track
        # 1. of the max number of nodes it can hold
        self.max_nodes = limit
        # 2. the current number of nodes it is holding
        self.current_nodes = 0

        # 3 a doubly-linked list that holds the key-value entries in the correctorder
        self.dll = DoublyLinkedList()
        # 4 Create dic
        self.dict = { }


    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """


    def get(self, key):
        # key is not in dit return NON
        if key not in self.dict:
            return None

        node = self.dll.head
        while node is not None:
            if key == node.value[0]:
                self.dll.move_to_front(node)
                break
            node = node.next

        # return value
        return self.dict[key]

        """
        my_dic = 
        """



    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.

    self.dll.head.value = (key, value)
    self.dll.head.value = {key: value}
    self.dll.head.value = [key, value]
    """
    def set(self, key, val):
         # 7 if key is already stored, overwrite old value
        if key in self.dict: 
            # overwrite in dictionary
            self.dict[key] = val
            # overwrite in the dll
            # iterate across and find the node to be updated
            node = self.dll.head
            while node is not None:
                # check key equality
                if key == node.value[0]:
                    # and update the value
                    node.value[1]= val
                    # move to head of dll
                    self.dll.move_to_front(node)
                    break
     
                node = node.next

        
        # 5 handle case where we are already full, if full delete the tail
        else:  
            if self.current_nodes == self.max_nodes:
                # delete something delete leaste recently used data
                node = self.dll.tail
                old_key = node.value[0]
                self.dll.remove_from_tail()
    
                # delete from dict
                del self.dict[old_key]
                # similiar
                # self.dict.pop(old_key)
                self.current_nodes -= 1

                # other add this key
                # 6 add to cache
            self.dict[key] = val
            self.dll.add_to_head([key,val])
        
                # Need to keep track of the current nodes
            self.current_nodes += 1
        
       


    