class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return int(key) % self.size

    def insert(self, key, item):
        hash_index = self._hash(key)
        self.table[hash_index].append((key, item))

    def retrieve(self, key):
        hash_index = self._hash(key)
        for k, i in self.table[hash_index]:
            if k == key:
                return i
        return None
