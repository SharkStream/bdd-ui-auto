import logging
import os
import sys
from datetime import datetime


class CustomFormatter(logging.Formatter):
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    RESET = '\033[0m'

    LEVEL_COLORS = {
        logging.ERROR: RED,
        logging.WARNING: YELLOW,
        logging.INFO: MAGENTA,
        logging.DEBUG: CYAN,
    }

    def format(self, record):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = record.getMessage()
        log_line = f"{timestamp} | {message}"

        color = self.LEVEL_COLORS.get(record.levelno, self.MAGENTA)
        log_line = f"{color}{log_line}{self.RESET}"

        return log_line


class DebugNoiseFilter(logging.Filter):
    """Filters out known debugger/threading noise from log output."""

    _default_noise_keywords = [
        "pydevd", "Exception ignored",
        "threading.py", "current_thread", "Using selector"
    ]

    def filter(self, record):
        message = record.getMessage()
        keywords = os.environ.get("LOG_FILTER_KEYWORDS")
        if keywords:
            noise_keywords = [k.strip() for k in keywords.split(",")]
        else:
            noise_keywords = self._default_noise_keywords
        if any(keyword in message for keyword in noise_keywords):
            return False
        return True


def setup_logger(name="test_framework", level=logging.INFO):
    """Setup and return a custom logger with the specified format."""

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    console_handler.setFormatter(CustomFormatter())

    if os.environ.get("LOG_FILTER", "1") == "1":
        console_handler.addFilter(DebugNoiseFilter())

    logger.addHandler(console_handler)
    return logger


# Create a default logger instance
default_logger = setup_logger()


def log_info(message):
    default_logger.info(message)


def log_error(message):
    default_logger.error(message)


def log_warning(message):
    default_logger.warning(message)


def log_debug(message):
    default_logger.debug(message)


def log_success(message):
    default_logger.info(f"✅ {message}")


def log_failure(message):
    default_logger.error(f"❌ {message}")


def log_info_emoji(emoji, message):
    default_logger.info(f"{emoji} {message}")


def log_error_emoji(emoji, message):
    default_logger.error(f"{emoji} {message}")
