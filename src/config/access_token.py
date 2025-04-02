
"""
    Get bearer token form initalization API
    Add bearer token in redis with expiraty date
"""
class AccessToken:
    '''
    AccessToken class to manage the access token for the API.
    It includes methods to check if the token is valid and to refresh the token.
    '''
    def __init__(self, token: str, expires_in: int):
        self.token = token
        self.expires_in = expires_in

    def is_valid(self) -> bool:
        '''
        Check if the token is still valid based on the expiration time.
        Returns True if the token is valid, False otherwise.
        '''
        # Check if the token is still valid based on the expiration time
        return self.expires_in > 0

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
