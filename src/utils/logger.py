"""
=========================================================
PROJECT ERYN
Logger
=========================================================
"""

import logging
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from config.config import LOG_FILE


def setup_logger() -> logging.Logger:
    """
    Configure and return the main ERYN logger.
    """

    # Create logs folder if it does not exist
    Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("ERYN")

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] %(message)s",
        datefmt="%d-%m-%Y %H:%M:%S",
    )

    # File Logger
    file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    file_handler.setFormatter(formatter)

    # Console Logger
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.info("Logger initialized successfully.")

    return logger