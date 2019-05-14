#!python

from trie import PrefixNode, PrefixTree
import unittest

class PrefixTreeTest(unittest.TestCase):
  
	def test_insert(self):
		tree = PrefixTree()
		tree.insert('1','0.05')



if __name__ == '__main__':
    unittest.main()
