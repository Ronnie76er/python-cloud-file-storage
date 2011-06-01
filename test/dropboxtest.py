import unittest
from pythoncloudfilestorage.client.client import FileStorageClient
from pythoncloudfilestorage.plugins.DropboxOfficialApi import DropboxOfficialApi

class TestDropBox(unittest.TestCase):
    
    def testApi(self):
        api = DropboxOfficialApi('testing.ini')
        
        myClient = FileStorageClient(api)
        
        for key in ['server', 'port', 'consumer_key', 'consumer_secret', 'verifier']:
            assert key in api.config, "Key %s is not set in config/testing.ini." % key

        
        myClient.sendFile('testfile.txt')
        
        
        
        
if __name__ == '__main__':
    unittest.main()