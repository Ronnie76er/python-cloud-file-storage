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
        self.config = config
    
    def authenticate(self):
        authenticator = auth.Authenticator(self.config)
        
        token = authenticator.obtain_request_token()
        print authenticator.build_authorize_url(token)
        
        tmp = raw_input("Hit enter when you've authorized it")
        
        access_token = authenticator.obtain_access_token(token, None)
        
        self.client = client.DropboxClient(self.server,
                                           self.content_server,
                                           self.port,
                                           authenticator,
                                           access_token)
        
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
    
        
