class HashTable:
    """
    This class represents a hash table data structure.
    It uses separate chaining to handle hash collisions.
    """

    def __init__(self, size):
        """
        The constructor for the HashTable class.
        It initializes the size of the hash table and creates an empty hash table.
        """
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        """
        This function implements a simple hash function.
        It takes a key and returns a hash index which is the key modulo the size of the hash table.
        """
        return int(key) % self.size

    def insert(self, key, item):
        """
        This function inserts a key-value pair into the hash table.
        It uses the hash function to determine the hash index for the key, and then appends the key-value pair to the list at that index.
        """
        hash_index = self._hash(key)
        self.table[hash_index].append((key, item))

    def retrieve(self, key):
        """
        This function retrieves a value from the hash table using its key.
        It uses the hash function to determine the hash index for the key, and then searches the list at that index for the key-value pair.
        If the key is found, it returns the corresponding value. If the key is not found, it returns None.
        """
        hash_index = self._hash(key)
        for k, i in self.table[hash_index]:
            if k == key:
                return i
        return None

    def remove(self, key):
        """
        This function removes a key-value pair from the hash table.
        It uses the hash function to determine the hash index for the key, and then removes the key-value pair from the list at that index.
        """
        hash_index = self._hash(key)
        self.table[hash_index] = [(k, i) for k, i in self.table[hash_index] if k != key]
