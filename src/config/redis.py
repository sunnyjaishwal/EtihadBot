"""
Redis configuration module.
This module is responsible for managing the Redis connection settings.
It includes the Redis host, port, and database number.
It also provides a function to create a Redis client instance.
This module is intended to be used in conjunction with other modules 
that require Redis functionality.
"""

import redis
class RedisClient:
    """
    RedisClient class to manage the Redis connection settings.
    It includes methods to create a Redis client instance.
    """
    def __init__(self, logger, host='localhost', port=8084, db=0):
        self.logger = logger
        self.host = host
        self.port = port
        self.db = db

    def create_client(self):
        """
        Create a Redis client instance.
        Returns:
            redis.StrictRedis: The Redis client instance.
        """
        self.logger.info(f"Creating Redis client with host: {self.host}, port: {self.port}, db: {self.db}")
        try:
            client = redis.StrictRedis(host=self.host, port=self.port, db=self.db, decode_responses=True)
            client.ping()  # Test the connection
            self.logger.info("Redis client created successfully.")
        except redis.ConnectionError as e:
            self.logger.error(f"Failed to connect to Redis: {e}")
            raise
        except Exception as e:
            self.logger.error(f"An error occurred while creating Redis client: {e}")
            raise
        return client

    def set_cache(self, key, value, expiry=None):
        """
        Set a cache value in Redis.
        Parameters:
            key (str): The cache key.
            value (str): The cache value.
            expiry (int): The expiration time in seconds. Default is None (no expiration).
        """
        client = self.create_client()
        self.logger.info("Setting cache for key: Key, value, and expiry")
        if expiry:
            client.setex(key, expiry, value)
        else:
            client.set(key, value)

    def get_cache(self, key):
        """
        Get a cache value from Redis.
        Parameters:
            key (str): The cache key.
        Returns:
            str: The cache value.
        """
        client = self.create_client()
        return client.get(key)
