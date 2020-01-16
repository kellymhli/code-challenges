class HashTable():

    def __init__(self):
        """Instantiate hashtable object."""

        self.size = 10
        self.table = [[] for x in range(0, self.size)]


    def get_hash_idx(self, key):
        """Generate the hash index for a given key."""

        idx = hash(key) % self.size
        return idx


    def add_to_table(self, key, value):
        """Add key value pair to hash table."""

        hash_idx = self.get_hash_idx(key)
        present = False

        # Check if each key already in table, if so, update value if needed
        for i, kv in enumerate(self.table[hash_idx]):
            k, v = kv
            if k == key:
                if v != value:
                    self.table[hash_idx][i] = (key, value)
                    present = True

        # Add key value pair to table if not present
        if not present:
            self.table[hash_idx].append((key, value))


    def get_val(self, key):
        """Return the value associated with a key."""

        hash_idx = self.get_hash_idx(key)
        pairs = self.table[hash_idx]

        for kv in pairs:
            k, val = kv
            if k == key:
                return val

        raise KeyError(f"{key}")


    def is_old_enough_to_rent_car(self, key, value):
        """Simple test function to pass into map function."""

        if value > 25:
            return True

        return False


    def map(self, func):
        """Return a new hashtable with that passes key value pairs through a function."""
        mapped_tbl = HashTable()

        # Iterate through each key value pair in existing table
        # and pass through the function
        for lst in self.table:
            for kv in lst:
                k, v = kv
                try:
                    result = func(k, v)
                    mapped_tbl.add_to_table(k, result)
                except:
                    pass

        return mapped_tbl


Table = HashTable()
Table.add_to_table('stephen', 10)
Table.add_to_table('kelly', 2)
Table.add_to_table('lisa', 30)
Table.add_to_table('kelly', 22)
Table.add_to_table('isaac', 38)

print(Table.get_val('stephen'))
print(Table.get_val('kelly'))
print(Table.table)

print(Table.map(Table.is_old_enough_to_rent_car).table)