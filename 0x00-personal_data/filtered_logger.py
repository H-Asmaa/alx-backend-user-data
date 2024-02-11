#!/usr/bin/env python3
"""
0x00-personal_data
"""
import re
from typing import List
import logging

PII_FIELDS = ("email", "phone", "ssn", "password", "ip")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """A function that returns the log message obfuscated."""
    for field in fields:
        pattern = rf"{field}=\S+?(?={re.escape(separator)}|$)"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """A function that returns a logging.Logger object."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.propagate = False
    return logger


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """The method init of the class."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """A method that filters incoming log records."""
        return filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
        )
