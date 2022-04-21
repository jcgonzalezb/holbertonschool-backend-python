#!/usr/bin/env python3
"""
This project module contains a type-annotated function that takes a list 
of floats as argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This is a method that takes a list of floats
    as argument and returns their sum as a float.
    Returns:
        A sum of floats as a float.
    """
    total: int = 0
    for ele in range(0, len(input_list)):
        total = total + input_list[ele]

    return float(total)
