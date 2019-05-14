#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        self.buckets = [LinkedList() for i in range(init_size)]
        self.size = 0  # Number of key-value entries

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        return hash(key) % len(self.buckets)

    def load_factor(self):
        """Return the load factor, the ratio of number of entries to buckets"""
        # ! Best case runtime = O(1), attribute properties already known.
        
        return self.size / len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table."""
        # ! Runtime = O(n), n is number of entries bucket
        # ! will tend towrads O(1) given a good hash func
        # Collect all keys in each of the buckets

        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        # ! Runtime = O(n), n is number of entries in a bucket
        # ! will tend towards O(1) given a good hash func
        # Collect all values in each of the buckets
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all entries (key-value pairs) in this hash table."""
        # ! Runtime = O(n), n is number of entries in a bucket
        # ! will tend towards O(1) given a good hash func
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets"""
        # ! Runtime = O(1), class attribute
        
        return self.size

    def contains(self, key):
        """Return True if this hash table contains the given key, or False."""
        # ! Runtime = O(n), n is number of entries in a bucket
        # ! will tend towards O(1) given a good hash func

        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        return entry is not None  # True or False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # ! Runtime = O(n)
        # ! tends towards O(1) given a good hash func

        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Return the given key's associated value
            assert isinstance(entry, tuple)
            assert len(entry) == 2
            return entry[1]
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value."""
        # ! Runtime = O(n), n is number of entries in a bucket
        # ! will tend towards O(1) given a good hash func

        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        # Check if an entry with the given key exists in that bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # In this case, the given key's value is being updated
            # Remove the old key-value entry from the bucket first
            bucket.delete(entry)
            self.size -= 1
        # Insert the new key-value entry into the bucket in either case
        bucket.append((key, value))
        self.size += 1
        # TODO: Check if the load factor exceeds a threshold such as 0.75 (ASK ALAN ABOUT LOAD SIZE FACTOR)
        if self.load_factor() > 0.75:
            # If so, automatically resize to reduce the load factor
            self._resize()

    def delete(self, key):
        """Delete the given key and its associated value, or raise KeyError."""

        # ! Runtime = O(n), n is number of entries in a bucket
        # ! will tend towards O(1) given a good hash func

        # Find the bucket the given key belongs in
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Find the entry with the given key in that bucket, if one exists
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:  # Found
            # Remove the key-value entry from the bucket
            bucket.delete(entry)
            self.size -= 1
        else:  # Not found
            raise KeyError('Key not found: {}'.format(key))

    def _resize(self, new_size=None):
        """Resize this hash table's buckets and rehash all key-value entries.
        Should be called automatically when load factor exceeds a threshold
        such as 0.75 after an insertion (when set is called with a new key)."""

        print("THIS IS THE RESIZE FUNC")

        # ! Runtime = O(n), n is number of entries in a bucket
        # ! will tend towards O(1) given a good hash func

        # If unspecified, choose new size dynamically based on current size
        if new_size is None:
            new_size = len(self.buckets) * 2  # Double size

        # Option to reduce size if buckets are sparsely filled (low load factor)
        elif new_size is 0:
            new_size = len(self.buckets) / 2  # Half size

        # Get a list to temporarily hold all current key-value entries
        items = self.items()
        print("HELLO")
        print(items)
        
        # Create a new list of new_size total empty linked list buckets
        self.__init__(new_size)

        # Insert each key-value entry into the new list of buckets,
        # which will rehash them into a new bucket index based on the new size
        for key, value in items:
            self.set(key, value)
        

def test_hash_table():
    ht = HashTable(4)
    print('HashTable: ' + str(ht))

    print('Setting entries:')
    ht.set('I', 1)
    print('set(I, 1): ' + str(ht))
    ht.set('V', 5)
    print('set(V, 5): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))
    ht.set('X', 10)
    print('set(X, 10): ' + str(ht))
    ht.set('L', 50)  # Should trigger resize
    print('set(L, 50): ' + str(ht))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))

    print('Getting entries:')
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('get(L): ' + str(ht.get('L')))
    print('contains(X): ' + str(ht.contains('X')))
    print('contains(Z): ' + str(ht.contains('Z')))

    print('Deleting entries:')
    ht.delete('I')
    print('delete(I): ' + str(ht))
    ht.delete('V')
    print('delete(V): ' + str(ht))
    ht.delete('X')
    print('delete(X): ' + str(ht))
    ht.delete('L')
    print('delete(L): ' + str(ht))
    print('contains(X): ' + str(ht.contains('X')))
    print('size: ' + str(ht.size))
    print('length: ' + str(ht.length()))
    print('buckets: ' + str(len(ht.buckets)))
    print('load_factor: ' + str(ht.load_factor()))


if __name__ == '__main__':
    test_hash_table()
