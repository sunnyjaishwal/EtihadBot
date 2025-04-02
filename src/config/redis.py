"""
Redis client to manage Redis operations.
It includes methods to get and set data in Redis.
"""
# Redis client to get and set data in Redis
class RedisClient:
    """
    RedisClient class to manage Redis operations.
    It includes methods to get and set data in Redis.
    """
    def __init__(self, logger, host='localhost', port=6379, db=0):
        self.logger = logger
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = None
        print("Redis constructor initiated")
        self.logger.info("Redis constructor initiated")
        # Uncomment the following line to initialize the Redis client
        #self.redis_client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)

    def get(self, key):
        """
        Get value from Redis by key.
        Parameters:
            key (str): The key to retrieve the value for.
        Returns:
            str: The value associated with the key.
        """
        return self.redis_client.get(key)

    def set(self, key, value, expiry=None):
        """
        Set value in Redis with an optional expiration time.
        Parameters:
            key (str): The key to set the value for.
            value (str): The value to set.
            expiry (int): Optional expiration time in seconds.
        """
        if expiry:
            self.redis_client.setex(key, expiry, value)
        else:
            self.redis_client.set(key, value)
