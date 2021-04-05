import unittest
from index import index

class TestIndex(unittest.TestCase):

    def test_build(self):
        index = index()
        index.build()
        
    def test_search(self):
        index = index()
        index.build()
        hello = index.search('Hello')
        self.assertEqual(hello['occurences'], 5)

if __name__ == '__main__':
    unittest.main()