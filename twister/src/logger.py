import logging
from colorama import Fore, Style, init

# Initialize Colorama for cross-platform color support
init(autoreset=True)

class ColorFormatter(logging.Formatter):
    """
    Custom formatter that adds color to the log level name based on its severity.
    """
    COLORS = {
        'DEBUG': Fore.BLUE,
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.MAGENTA,
    }
    
    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record, adding color to the level name.
        
        Args:
            record (logging.LogRecord): The log record to format.
        
        Returns:
            str: The formatted log message.
        """
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = self.COLORS[levelname] + levelname + Style.RESET_ALL
        return super().format(record)

class Logger:
    """
    Logger class that encapsulates Python's logging configuration.
    
    This logger uses the ColorFormatter to display logs with colored log level names,
    and includes a timestamp in the log messages. The log level can be set using the
    'loglevel' parameter during initialization.
    """
    def __init__(self, name: str = __name__, loglevel: int = logging.DEBUG) -> None:
        """
        Initialize the Logger instance.
        
        Args:
            name (str): The name of the logger. Defaults to __name__.
            loglevel (int): The logging level (e.g., logging.DEBUG, logging.INFO). Defaults to logging.DEBUG.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(loglevel)
        
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            handler.setLevel(loglevel)
            formatter = ColorFormatter(
                fmt="%(asctime)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
    
    def debug(self, *messages: any) -> None:
        """
        Log a message with DEBUG level.
        
        Args:
            *messages (tuple): A tuple of messages to be concatenated and logged.
        """
        message = " ".join(str(m) for m in messages)
        self.logger.debug(message)
    
    def info(self, *messages: any) -> None:
        """
        Log a message with INFO level.
        
        Args:
            *messages (tuple): A tuple of messages to be concatenated and logged.
        """
        message = " ".join(str(m) for m in messages)
        self.logger.info(message)
    
    def warning(self, *messages: any) -> None:
        """
        Log a message with WARNING level.
        
        Args:
            *messages (tuple): A tuple of messages to be concatenated and logged.
        """
        message = " ".join(str(m) for m in messages)
        self.logger.warning(message)
    
    def error(self, *messages: any) -> None:
        """
        Log a message with ERROR level.
        
        Args:
            *messages (tuple): A tuple of messages to be concatenated and logged.
        """
        message = " ".join(str(m) for m in messages)
        self.logger.error(message)
    
    def critical(self, *messages: any) -> None:
        """
        Log a message with CRITICAL level.
        
        Args:
            *messages (tuple): A tuple of messages to be concatenated and logged.
        """
        message = " ".join(str(m) for m in messages)
        self.logger.critical(message)

if __name__ == "__main__":
    log = Logger("MyLogger", loglevel=logging.DEBUG)
    log.debug("This is a", "DEBUG message.")
    log.info("This is an", "INFO message.")
    log.warning("This is a", "WARNING message.")
    log.error("This is an", "ERROR message.")
    log.critical("This is a", "CRITICAL message.")
