#!/usr/bin/env python3
"""
0x00-personal_data
"""
import re
from typing import List

import logging


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """A function that returns the log message obfuscated."""
    for field in fields:
        pattern = rf"{field}=\S+?(?={re.escape(separator)}|$)"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List):
        """The method init of the class."""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """A method that filters incoming log records."""
        return filter_datum(
            self.fields, self.REDACTION, super().format(record), self.SEPARATOR
        )
