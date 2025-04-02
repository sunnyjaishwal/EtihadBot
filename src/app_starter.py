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
        self.redis_client = RedisClient(self.logger)

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

    def _setup_database(self):
        # Placeholder for database setup logic
        self.logger.info("Setting up database connection...")
        time.sleep(1)  # Simulate database setup time
        self.logger.info("Database connection established.")

    def _get_tokens(self):
        # Placeholder for token retrieval logic
        self.redis_client.set_cache("x-d-token", "get_x-d-token_from_redis", 3600)
        # Placeholder for token retrieval logic
        self.logger.info("Retrieving tokens...")
        print(self.redis_client.get_cache("x-d-token"))

    def _get_proxy(self):
        pass

    def _get_fingerprint(self):
        pass

    def start_bot(self):
        """
        Start the server.
        """
        # Placeholder for server startup logic
        self.logger.info("Starting scraper...")
        self._get_tokens()
        self._get_proxy()
        self._get_fingerprint()
        time.sleep(1)  # Simulate server startup time
        self.logger.info("Scraper started.")

    def run(self):
        """
        Run the application.
        """
        self._setup_database()
        self.start_bot()
        self.logger.info("Application is running.")


if __name__ == "__main__":
    configurations = {
        # "db_host": os.getenv("DB_HOST", "localhost"),
        # "db_port": os.getenv("DB_PORT", "5432"),
        # "db_user": os.getenv("DB_USER", "user"),
        # "db_password": os.getenv("DB_PASSWORD", "password"),
        # Uncomment and configure the following keys as needed
        "db_name": os.getenv("DB_NAME", "database"),
        "redis_host": os.getenv("REDIS_HOST", "localhost"),
        "redis_port": os.getenv("REDIS_PORT", "6379"),
        "redis_password": os.getenv("REDIS_PASSWORD", None),
    }

    app_starter = AppStarter(configurations)
    app_starter.setup_logging()
    app_starter.run()
