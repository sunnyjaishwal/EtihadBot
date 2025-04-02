"""
This is the entry point for the application.
It initializes the application, sets up the database connection,
and starts the server.
It also includes a function to run the application in development mode.
"""
import os
import logging
import time

from config.redis import RedisClient
# from utilities.cookie_manager import CookieManager
# from utilities.proxy_manager import ProxyManager
# from validators.request_validator import RequestValidator
# from validators.response_validator import ResponseValidator

class AppStarter:
    """
    AppStarter class to initialize and run the application.
    It includes methods to set up the database connection,
    start the server, and run the application in development mode.
    """
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def setup_logging(self):
        """
        Set up logging configuration.
        """
        log_file_path = os.path.join(os.getcwd(), "etihad_bot.log")
        logging.basicConfig(
            level=logging.INFO,  # Set the log level
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file_path),  # Log to the root-level file
                logging.StreamHandler()             # Log to the console
            ]
        )
        self.logger.info("Logging initialized. Logs will be written to the root file and console.")

    def setup_database(self):
        """
        Set up the database connection.
        """
        # Placeholder for database setup logic
        self.logger.info("Setting up database connection...")
        time.sleep(1)  # Simulate database setup time
        self.logger.info("Database connection established.")

    def get_tokens(self):
        """
        Get tokens from the redis.
        """
        RedisClient(self.logger)
        # Placeholder for token retrieval logic
        self.logger.info("Retrieving tokens...")
        x_d_token = "get_x-d-token_from_redis" #
        bearer_access_token = "get_bearer_access_token_from_redis"
        self.logger.info("Tokens retrieved.")
        self.logger.info(f"X-D-Token: {x_d_token}")
        self.logger.info(f"Bearer Access Token: {bearer_access_token}")

    def start_bot(self):
        """
        Start the server.
        """
        # Placeholder for server startup logic
        self.logger.info("Starting scraper...")
        self.get_tokens()
        time.sleep(1)  # Simulate server startup time
        self.logger.info("Scraper started.")

    def run(self):
        """
        Run the application.
        """
        self.setup_database()
        self.start_bot()
        self.logger.info("Application is running.")


if __name__ == "__main__":
    configurations = {
        "db_host": os.getenv("DB_HOST", "localhost"),
        "db_port": os.getenv("DB_PORT", "5432"),
        "db_user": os.getenv("DB_USER", "user"),
        "db_password": os.getenv("DB_PASSWORD", "password"),
        # Uncomment and configure the following keys as needed
        # "db_name": os.getenv("DB_NAME", "database"),
        # "redis_host": os.getenv("REDIS_HOST", "localhost"),
        # "redis_port": os.getenv("REDIS_PORT", 6379),
        # "redis_password": os.getenv("REDIS_PASSWORD", None),
    }

    app_starter = AppStarter(configurations)
    app_starter.setup_logging()
    app_starter.run()
