"""
File storage client API
"""


class FileStorageClient:
    
    
    def __init__(self, plugin=None):
        print "Testing"
        self.plugin = plugin
        
        
    def setPlugin(self, plugin):
        self.plugin = plugin
        
        