import unittest
from pythoncloudfilestorage.client.client import FileStorageClient

class TestDropBox(unittest.TestCase):
    
    def testApi(self):
        self.assertTrue(True)
        myClient = FileStorageClient()
        
        myClient.sendFile('testfile.txt')
        
        
        
        
if __name__ == '__main__':
    unittest.main()