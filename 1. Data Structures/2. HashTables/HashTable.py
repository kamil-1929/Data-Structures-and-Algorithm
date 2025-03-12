# Hash table
# what is HashTable ? 
# A hash table is a data structure that stores key-value pairs in an array using a hash function
# to map keys to indices of the array.
# Hash tables are also known as hash maps, dictionaries, or associative arrays.
# They are used to implement many other data structures, such as sets and graphs.
# Hash tables are useful when you need to store and retrieve data based on a unique identifier, such
 # as a string or an integer.
 
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    # Hash function to compute the index for a given key
    def _hash(self, key):
        return hash(key) % self.size
    
    # Method to insert a key-value pair into the hash table
    def insert(self, key, value):
        index = self._hash(key)
        self.table[index] = value
    
    # Method to retrieve the value associated with a given key from the hash table
    def get(self, key):
        index = self._hash(key)
        return self.table[index]
    
    # Method to delete a key-value pair from the hash table
    def delete(self, key):
        index = self._hash(key)
        self.table[index] = None

# Example usage
ht = HashTable()

ht.insert("apple", 10)
ht.insert("banana", 2)
ht.insert("orange", 3)

print(ht.get("apple"))  # Output: 10

ht.delete("banana")
print(ht.get("banana"))  # Output: None


class HashTable1:
    def __init__(self, size=10):
        self.size = size
        self.table =[[] for _ in range(size)]
        
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        
        # check if key already exists and update it
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return 
        # If the key does not exist, append a new key-value pair
        self.table[index].append((key, value))          
    
    def get(self, key):
        index = self._hash(key)
        for k,v in self.table[index]:
            if k == key:
                return v
        return None 
    
    def delete(self, key):
        index = self._hash(key)
        for i, (k,v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return True
        return False # Key not found 
    
if __name__ == "__main__":
    ht1 = HashTable1()
    ht1.insert("apple", 1)
    ht1.insert("banana", 2)
    ht1.insert("orange", 3)
    
    print(ht1.get("apple"))
    print(ht1.get("banana"))
    print(ht1.get("grape"))
    
    ht1.delete("banana")
    print(ht1.get("banana"))
    
    ht1.insert("grape", 3)
    ht1.insert("melon", 3)
        
    print(ht1.get("grape"))
    print(ht1.get("melon"))
    
    
# HashTable Dynamic Resizing
# To improve performance, we can implement dynamic resizing. When the load factor 
# (number of elements divided by the size of the table) exceeds a certain threshold, 
# we can resize the table to a larger size and rehash all existing keys.