import unittest
from pythoncloudfilestorage.client.client import FileStorageClient
from pythoncloudfilestorage.plugins.DropboxOfficialApi import DropboxOfficialApi
from ConfigParser import SafeConfigParser

class TestDropBox(unittest.TestCase):
    
    filename = 'testing.ini'
    
    def testApi(self):
        
        config = SafeConfigParser()
        configFile = open(self.filename, 'r')
        config.readfp(configFile)
        configDict = dict(config.items('auth'))
        
        api = DropboxOfficialApi(configDict['consumer_key'], configDict['consumer_secret'], configDict)
        
        myClient = FileStorageClient(api)
        
        print myClient.getAuthorizationUrl()
        tmp = raw_input("Hit enter when you've authorized it")
        
        myClient.authenticate()
        
        
        
        resp = myClient.sendFile('testfile.txt')
        assert resp.status == 200
        
        resp = myClient.getFile('testfile.txt')
        assert resp.status == 200
        
        resp = myClient.deleteFile('testfile.txt')
        assert resp.status == 200
        
        resp = myClient.getFile('testfile.txt')
        assert resp.status != 200
        
        
        
        
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestDropBox)
    unittest.TextTestRunner(verbosity=2).run(suite)