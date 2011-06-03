"""
File storage client API
"""


class FileStorageClient:
    
    
    def __init__(self, plugin=None):
        self.plugin = plugin
            
    def getAuthorizationUrl(self):
        return self.plugin.getAuthorizationUrl()
        
    def authenticate(self):
        return self.plugin.authenticate()
        
    def setPlugin(self, plugin):
        self.plugin = plugin
        
    def sendFile(self, name):
        return self.plugin.sendFile(name)

    def getFile(self, name):
        return self.plugin.getFile(name)
        
    def deleteFile(self, name):
        return self.plugin.deleteFile(name)
        
        