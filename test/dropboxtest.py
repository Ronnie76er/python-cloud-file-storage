import unittest
from pythoncloudfilestorage.client.client import FileStorageClient
from pythoncloudfilestorage.plugins.DropboxOfficialApi import DropboxOfficialApi

class TestDropBox(unittest.TestCase):
    
    def testApi(self):
        self.assertTrue(True)
        myClient = FileStorageClient(DropboxOfficialApi())
        
        myClient.sendFile('testfile.txt')
        
        
        
        
if __name__ == '__main__':
    unittest.main()