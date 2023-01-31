import array


class BloomFilter(object):
    """A simple BloomFilter applicable to a set S of ints"""
    # def __init__(self, Mbits=11):   #Mbits=11のとき、500は偽陽性となっていた
    def __init__(self, Mbits=256):    #Mbits=256のとき、500はFalse
        if __name__ == '__main__':
            self.Mbits = Mbits
            self.abits = array.array('b', [0]) * self.Mbits
            self.kHash = 2
            self.Nadds = 0

    def _element_index(self, element):
        bitelm = bin(element)[2:]
        return [self._hTindex(self._h1(bitelm), self.Mbits), self._hTindex(self._h2(bitelm), self.Mbits)]

    def _h1(self, x):
        """
        A simple hash function which takes bit array x as input and
        rerturns a new bit array created using odd number index bits of x."""
        return int("".join([v for i, v in enumerate(x) if i % 2 == 0]), 2)

    def _h2(self, x):
        return int("".join([v for i, v in enumerate(x) if i % 2 == 1]), 2)

    def _hTindex(self, hash, Mbits):
        return hash % Mbits

    def add(self, element):
        for i in self._element_index(element):
            self.abits[i] = 1
        self.Nadds = self.Nadds + 1

    def query(self, element):
        for i in self._element_index(element):
            if self.abits[i] == 0:
                return False
        return True

if __name__ == '__main__':
    filter = BloomFilter()

    S = [12000, 9000, 22011, 5551, 4953, 6582, 5929, 5662, 8888, 1382]

    for element in S:
        filter.add(element)

    print('Is %d part of S?: %s'% (44, filter.query(44)))
    print('Is %d part of S?: %s'% (9000, filter.query(9000)))
    print('Is %d part of S?: %s'% (1500, filter.query(1500)))
    print('Is %d part of S?: %s'% (5662, filter.query(5662)))
    print('Is %d part of S?: %s'% (500, filter.query(500)))