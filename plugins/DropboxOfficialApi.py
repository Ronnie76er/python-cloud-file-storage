from BasePluginApi import BasePluginApi
from dropbox import auth

class DropboxOfficialApi(BasePluginApi):
    
    def __init__(self, configFilename):
        self.configFilename = configFilename
    
    def authenticate(self):
        self.config = auth.Authenticator.load_config(self.configFilename)
