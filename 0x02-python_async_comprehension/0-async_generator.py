#!/usr/bin/env python3
"""
This project module contains a coroutine that takes no
arguments. The coroutine will loop 10 times, each time
asynchronously wait 1 second, then yield a random 
number between 0 and 10.
"""

import asyncio
import random


async def async_generator():
    """
    This is an asynchronous coroutine that takes in no
    arguments. The coroutine will loop 10 times, each
    time asynchronously wait 1 second, then yield a
    random number between 0 and 10.
    Returns:
        Random number between 0 and 10.
    """
    delay = 1
    for _ in range(10):
        await asyncio.sleep(delay)
        yield random.uniform(0, 10)
