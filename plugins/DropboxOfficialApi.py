from dropbox import auth, client

class DropboxOfficialApi():
    
    server = 'api.dropbox.com'
    content_server = 'api-content.dropbox.com'
    port = 80
    
    request_token_url = 'https://api.dropbox.com/0/oauth/request_token'
    access_token_url = 'https://api.dropbox.com/0/oauth/access_token'
    authorization_url = 'https://www.dropbox.com/0/oauth/authorize'
    trusted_access_token_url = 'https://api.dropbox.com/0/token'

    def __init__(self, consumer_key, consumer_secret, config):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.authenticator = auth.Authenticator(config)
    
    def authenticate(self):
        self.access_token = self.authenticator.obtain_access_token(self.token, None)
        
        self.client = client.DropboxClient(self.server,
                                           self.content_server,
                                           self.port,
                                           self.authenticator,
                                           self.access_token)
        
    def getAuthorizationUrl(self):
        self.token = self.authenticator.obtain_request_token()
        return self.authenticator.build_authorize_url(self.token)
        
        
    def requestAuthorization(self):
        print 'Something'
        
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
    
        
