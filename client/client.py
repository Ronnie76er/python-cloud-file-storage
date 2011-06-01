"""
File storage client API
"""


class FileStorageClient:
    
    
    def __init__(self, plugin=None):
        print "Testing"
        self.plugin = plugin
        if self.plugin != None:
            self.plugin.authenticate()
            
        
        
    def setPlugin(self, plugin):
        self.plugin = plugin
        
    def sendFile(self, name):
        print 'Not implemented yet'
        
        