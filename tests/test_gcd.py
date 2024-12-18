import sys
import os

from my_arithmetic_.gcd import gcd
import unittest

class TestGCD(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(101, 103), 1)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(0, 0), 0)

if __name__ == '__main__':
    unittest.main()

