from BasePluginApi import BasePluginApi
from dropbox import auth, client

class DropboxOfficialApi(BasePluginApi):
    
    def __init__(self, configFilename):
        self.configFilename = configFilename
    
    def authenticate(self):
        self.config = auth.Authenticator.load_config(self.configFilename)
        authenticator = auth.Authenticator(self.config)
        
        token = authenticator.obtain_request_token()
        print authenticator.build_authorize_url(token)
        
        tmp = raw_input("Hit enter when you've authorized it")
        
        access_token = authenticator.obtain_access_token(token, self.config['verifier'])
        
        print access_token
        
        self.client = client.DropboxClient(self.config['server'],
                                           self.config['content_server'],
                                           self.config['port'],
                                           authenticator,
                                           access_token)
        
    def sendFile(self, filename):
        f = open(filename)
        resp = self.client.put_file('dropbox', '/', f)
        return resp
            
            
    def getFile(self, filename):
        resp = self.client.get_file('dropbox', '/' + filename)
        return resp
    
    def deleteFile(self, filename):
        resp = self.client.file_delete('dropbox', '/' + filename)
        return resp
        
