#!/usr/bin/env python3
"""
This project module contains a type-annotated function
that takes a string and an int OR float v as arguments
and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This is a method that takes a string and an int OR
    float as arguments and returns a tuple.
    Returns:
        A tuple.
    """
    return (k, v * v)
