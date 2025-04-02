import requests
import redis

# Get X-D-Token from rubie api
# Add token in redis with expiraty date
class TokenManager:
    def __init__(self, api_url, redis_host='localhost', redis_port=6379):
        self.api_url = api_url
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

    def fetch_token(self):
        # Placeholder for logic to fetch token from the API
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json().get('token')
        else:
            raise Exception(f"Failed to fetch token: {response.status_code}")

    def store_token(self, token, expiry):
        # Placeholder for logic to store token in Redis with expiry
        self.redis_client.setex('x-d-token', expiry, token)

    def get_token(self):
        # Placeholder for logic to retrieve token from Redis or fetch a new one
        token = self.redis_client.get('x-d-token')
        if token:
            return token
        else:
            token = self.fetch_token()
            self.store_token(token, 3600)  # Example expiry time of 1 hour
            return token