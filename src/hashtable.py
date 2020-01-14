

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0
        self.original_capacity = capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        str_values = []
        for char in list(key):
            str_values.append(ord(char))

        # return hash(key)
        return sum(str_values)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]

        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
            self.count += 1
        else:    
            while node is not None:
                if node.key == key:
                    node.value = value
                    break
                if node.next is None:
                    node.next = LinkedPair(key, value)
                    self.count += 1
                    break
                else:
                    node = node.next
        if self.count >= self.capacity*0.7: self.resize()


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
 
        while node is not None:
            if node.key == key:
                # print(f'key: {node.key}, value: {node.value} - count: {self.count} - capacity: {self.capacity}')
                node.value = None
                self.count -= 1
                if self.count <= self.capacity*0.2: self.resize_smaller()
                return
            else:
                node = node.next
        print(f'Cannot remove, {key} not found.')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        node = self.storage[index]
 
        while node is not None:
            if node.key == key:
                return node.value
            else:
                node = node.next

        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity = self.capacity*2
        self.storage = [None] * self.capacity
        self.count = 0

        for node in old_storage:
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next

    def resize_smaller(self):
        if self.capacity > self.original_capacity:
            old_storage = self.storage
            self.capacity = self.capacity//2
            self.storage = [None] * self.capacity
            self.count = 0

            for node in old_storage:
                while node is not None and node.value is not None:
                    # print(f'insert: key: {node.key}, value: {node.value}, count: {self.count}')
                    self.insert(node.key, node.value)
                    node = node.next



test = HashTable(3)
test_hash = test._hash_mod("testing")
print(test_hash)

if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
