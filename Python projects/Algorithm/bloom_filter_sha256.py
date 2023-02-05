#!/usr/bin/env python3
import array, sys
from math import exp
from hashlib import sha224, sha256


class BloomFilter(object):
    def __init__(self, Mbits=48, kHash=9):
        """A simple BloomFilter applicable to a set S of ints"""
        self.Mbits = Mbits
        self.abits = array.array('b', [0]) * self.Mbits
        self.kHash = kHash
        self.Nadds = 0

    def _element_index(self, element):
        return [self._hTindex(self._hi(i, element)) for i in range(self.kHash)]

    def _hi(self, i, x):
        """
        _hi(x) = _h1(x) + i*_h2(x)
        """
        return self._sha256(x) + i * self._sha224(x)

    def _sha256(self, x):
        """
        Takes any value x as input, applies SHS256 hash function and returns an int.
        """
        return int(sha256(str(x).encode()).hexdigest(), 16)

    def _sha224(self, x):
        """
        Takes any value x as input, applies SHS256 hash function and returns an int.
        """
        return int(sha224(str(x).encode()).hexdigest(), 16)

    def _hTindex(self, hash):
        """
        Maps output of a hash function to a bit array index
        """
        return hash % self.Mbits

    def add(self, element):
        for i in self._element_index(element):
            self.abits[i] = 1
        self.Nadds = self.Nadds + 1

    def query(self, element):
        for i in self._element_index(element):
            if self.abits[i] == 0:
                return False
        return True

    def size(self):
        return sys.getsizeof(self.abits)

    def fp_prob(self):
        return (1 - exp(-(self.kHash * self.Nadds) / self.Mbits)) ** self.kHash

if __name__ == '__main__':
    filter = BloomFilter(Mbits=512, kHash=13)
    S = '''Alabama Alaska Arizona Arkansas California Colorado Connecticut
    Delaware Florida Georgia Hawaii Idaho Illinois Indiana Iowa Kansas
    Kentucky Louisiana Maine Maryland Massachusetts Michigan Minnesota
    Mississippi Missouri Montana Nebraska Nevada NewHampshire NewJersey
    NewMexico NewYork NorthCarolina NorthDakota Ohio Oklahoma Oregon
    Pennsylvania RhodeIsland SouthCarolina SouthDakota Tennessee Texas Utah
    Vermont Virginia Washington WestVirginia Wisconsin Wyoming'''.split(" ")

    for element in S:
        filter.add(element)

    print("False positive probability : %f" % filter.fp_prob())
    print("Original size for S in bytes: %d" % sys.getsizeof(S))
    print("Bloom filter's size in bytes: %d" % filter.size())
    print('Is %s part of S?: %s'% ("Alabama", filter.query("Alabama")))
    print('Is %s part of S?: %s'% ("NorthCarolina", filter.query("NorthCarolina")))
    print('Is %s part of S?: %s'% ("NorthCarolina", filter.query("NorthCarolina")))
    print('Is %s part of S?: %s'% ("West Delhi", filter.query("West Delhi")))
    print('Is %s part of S?: %s'% ("North Sydney", filter.query("North Sydney")))