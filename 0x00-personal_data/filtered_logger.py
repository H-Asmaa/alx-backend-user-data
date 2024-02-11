#!/usr/bin/env python3
"""
0x00-personal_data
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """A function that returns the log message obfuscated."""
    for field in fields:
        pattern = rf'{field}=\S+?(?={re.escape(separator)}|$)'
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message
