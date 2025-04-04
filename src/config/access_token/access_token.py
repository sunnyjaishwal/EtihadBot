
"""
    Get bearer token form initalization API
    Add bearer token in redis with expiry date
"""
import requests
import json
import os
import time

from base_token.base_token import BaseToken
class AccessToken:
    '''
    AccessToken class to manage the access token for the API.
    It includes methods to check if the token is valid and to refresh the token.
    '''
    def __init__(self,  api_url):
        ob = BaseToken()
        xd_token= ob.fetch_token()
        
        print(xd_token)
        self.api_url= api_url
        self.payload= 'client_id=TEAP1EPUAR97S1aWCpEkWe9L3VvhtBIK&client_secret=j9sP1PK9cEJKbL1o&fact=%7B%22keyValuePairs%22%3A%5B%7B%22key%22%3A%22flow%22%2C%22value%22%3A%22REVENUE%22%7D%2C%7B%22key%22%3A%22market%22%2C%22value%22%3A%22IN%22%7D%2C%7B%22key%22%3A%22originCity%22%2C%22value%22%3A%22DEL%22%7D%2C%7B%22key%22%3A%22originCountry%22%2C%22value%22%3A%22IN%22%7D%2C%7B%22key%22%3A%22currencyCode%22%2C%22value%22%3A%22%22%7D%2C%7B%22key%22%3A%22channel%22%2C%22value%22%3A%22DESKTOP%22%7D%5D%7D&grant_type=client_credentials'
        file_path= os.path.join('access_token', 'headers.json')
        with open(file_path, "r") as h:
            data= json.load(h)
        self.header= data
        self.header['x-d-token'] = xd_token
        print("******************************************")
        
        
        
    def fetch_access_token(self):
        
        response = requests.post(url= self.api_url, data= self.payload, headers= self.header, timeout=10)
        if response.status_code == 200:
            return response.json().get('access_token')
        else:
            raise Exception( f"Failed to fetch Exception111111111111 {response.status_code}")
   
    def refresh(self, new_token: str, new_expires_in: int):
        '''
        Refresh the token and update its expiration time.
        Parameters:
            new_token (str): The new token to set.
            new_expires_in (int): The new expiration time in seconds.
        '''
        # Update the token and its expiration time
        self.token = new_token
        self.expires_in = new_expires_in
        
if __name__ == '__main__':
    url = "https://api-des.etihad.com/v1/security/oauth2/token/initialization"
    object = AccessToken(url)
    print(object.fetch_access_token())
