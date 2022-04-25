#!/usr/bin/env python3
"""
This project module contains an asynchronous coroutine that
takes an integer argument with a default value of 10, waits
for a random delay (float) between 0 and 10 and returns it.
"""

import random


async def wait_random(max_delay: int = 10) -> float:
    """
    This is an asynchronous coroutine that takes a parameter
    (integer) and returns a random delay (float).
    Returns:
        Value of random delay (float).
    """
    i = random.uniform(0, max_delay)
    return i
