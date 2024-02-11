#!/usr/bin/env python3
"""
0x00-personal_data
"""
import re


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str):
    """A function that returns the log message obfuscated.
    Args:
        fields (list of strings) -- representing all fields to obfuscate.
        redaction (string) -- representing by what the field will be obfus-
            cated.
        message (string) -- representing the log line.
        separator (string) -- representing by which character is separating
            all fields in the log line (message).
    Returns:
        The log message obfuscated
    Rules:
        The function should use a regex to replace occurrences of certain field
        values.
        filter_datum should be less than 5 lines long and use re.sub to perform
        the substitution with a single regex.
    """
    for field in fields:
        pattern = rf'{field}=\S+?(?={re.escape(separator)}|$)'
        message = re.sub(pattern, f'{field}=xxx', message)
    return message
