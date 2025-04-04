
"""
This module is responsible for managing the X-D-Token used in API requests.
It includes functionality to fetch the token from the API, 
store it in Redis with an expiration time,
"""
import requests
import json
import os

# Get X-D-Token from rubie api
# Add token in redis with expiraty date
class BaseToken:
    '''
    TokenManager class to manage the X-D-Token for API requests.
    It includes methods to fetch the token from the API, store it in Redis,
    and retrieve it when needed.
    '''
    def __init__(self):
        self.api_url = "https://digital.etihad.com/rubie-Fease-no-sall-be-intome-Deat-seemselfe-Mot"
        header_file= os.path.join('base_token', 'headers.json')
        with open(header_file, "r") as h:
            data = json.load(h)
        self.header = data
        payload_file= os.path.join('base_token','payload.txt')
        with open(payload_file, "r") as p:
            body = p.read().strip()
        self.payload = body
        
    def fetch_token(self):
        '''
        Fetch the token from the API.
        Returns:
            str: The fetched token.
        '''
        response = requests.post(url=self.api_url, headers= self.header, data= self.payload, timeout=5)
        #print(response.text)
        with open("response.json", "w") as r:
            r.write(response.text)
        if response.status_code == 200:
            token= response.json().get('token')
            return token.strip()
        else:
            raise Exception(f"Failed to fetch token: {response.status_code}")

   

    def get_old_token(self):
        '''
        Retrieve the token from Redis or fetch a new one if it doesn't exist.'
        '''
        # Placeholder for logic to retrieve token from Redis or fetch a new one
        token = self.redis_client.get('x-d-token')
        if token:
            return token
        else:
            token = self.fetch_token()
            self.store_token(token, 3600)  # Example expiry time of 1 hour
            return token

if __name__ == '__main__':
     object = BaseToken()
     print(object.fetch_token())