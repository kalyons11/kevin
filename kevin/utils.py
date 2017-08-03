"""
Quick package utils script.
"""

import numpy as np


def strip_str(inp):
    """Helper method to strip a string of all non alphanumeric characters.

    Example:
    >>> x = 'Test-string123__:'
    >>> y = strip_str(x)
    >>> y
    >>> 'teststring123'

    Args:
        inp (str): -

    Returns:
        str: stripped output
    """

    return ''.join(ch.lower() for ch in inp if ch.isalnum())


def validate_iter(obj):
    """Helper method to validate that an object is at least a list
        or np.ndarray.

    Args:
        obj (unknown): any input

    Returns:
        2-tuple: iterable version of obj and bool indicator of whether
            or not obj was already an iterable
    """
    if isinstance(obj, (list, np.ndarray)):
        return obj, True

    return [obj], False
