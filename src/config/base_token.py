
"""
This module is responsible for managing the X-D-Token used in API requests.
It includes functionality to fetch the token from the API, 
store it in Redis with an expiration time,
"""
import requests
import redis

# Get X-D-Token from rubie api
# Add token in redis with expiraty date
class TokenManager:
    '''
    TokenManager class to manage the X-D-Token for API requests.
    It includes methods to fetch the token from the API, store it in Redis,
    and retrieve it when needed.
    '''
    def __init__(self, api_url, redis_host='localhost', redis_port=6379):
        self.api_url = api_url
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    def fetch_token(self):
        '''
        Fetch the token from the API.
        Returns:
            str: The fetched token.
        '''
        # Placeholder for logic to fetch token from the API
        response = requests.get(self.api_url, timeout=5)
        if response.status_code == 200:
            return response.json().get('token')
        else:
            raise Exception(f"Failed to fetch token: {response.status_code}")

    def store_token(self, token, expiry):
        '''
        Store the token in Redis with an expiration time.
        Parameters:
            token (str): The token to store.
            expiry (int): The expiration time in seconds.
        '''

        # Placeholder for logic to store token in Redis with expiry
        self.redis_client.setex('x-d-token', expiry, token)

    def get_token(self):
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
