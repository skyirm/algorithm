

class HashTable:

    def __init__(self) -> None:
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(hashvalue, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def get(self, key):
        start_slot = self.hashfunction(key, len(self.slots))

        position = start_slot
        while True:
            if self.slots[position] == None:
                return None
            if self.slots[position] == key:
                return self.data[position]
            position = self.rehash(position, len(self.slots))
            if position == start_slot:
                return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

h=HashTable()
h[31]='cat'
h[20]='mow'
print(h[31], h[20],h[9])