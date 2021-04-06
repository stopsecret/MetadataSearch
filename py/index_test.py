import unittest
from index import index

TEST_DIRECTORY = 'test_index_directory'
#TEST_DIRECTORY = r'C:\Users\BAA16\OneDrive - Unum\Documents\Organized\Salesforce Metadata Backups\metadata 2021-02-02'
class TestIndexing(unittest.TestCase):
    def test_build(self):
        i = index()
        i.build(TEST_DIRECTORY)

class TestSearching(unittest.TestCase):
    index = index()
    
    @classmethod
    def setUpClass (self):
        self.index.build(TEST_DIRECTORY)

    def test_search(self):
        hello = self.index.search('Hello')
        self.assertEqual(hello['result'], 'success')
        self.assertEqual(hello['words']['hello']['count'], 5)
        self.assertEqual(hello['words']['hello']['filecounts']['test_index_directory\\dir1\\testing.txt'], 5)

    def test_search_mixedcase(self):
        hello = self.index.search('heLLo')
        self.assertEqual(hello['result'], 'success')
        self.assertEqual(hello['words']['hello']['count'], 5)
        self.assertEqual(hello['words']['hello']['filecounts']['test_index_directory\\dir1\\testing.txt'], 5)

    def test_search_partial(self):
        hello = self.index.search('howd')
        self.assertEqual(hello['result'], 'success')
        self.assertEqual(hello['words']['howdy']['count'], 1)
        self.assertEqual(hello['words']['howdy']['filecounts']['test_index_directory\\dir2\\another.txt'], 1)

    def test_search_notfound(self):
        notfound = self.index.search('Buffalo')
        self.assertEqual(notfound['result'], 'notfound')

    def test_search_as_files(self):
        result = self.index.search_files('Hello')
        self.assertEqual(result['test_index_directory\\dir1\\testing.txt']['count'], 5)
        

if __name__ == '__main__':
    unittest.main()