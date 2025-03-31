import logging

def setup_logging():
    """Configure logging with a more detailed format"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('airline.log'),
            logging.StreamHandler()
        ]
    )
    logging.info("Logging system initialized")
    