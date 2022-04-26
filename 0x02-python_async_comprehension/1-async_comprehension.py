#!/usr/bin/env python3
"""
This project module contains a coroutine that takes no
arguments. The coroutine will loop 10 times, each time
asynchronously wait 1 second, then yield a random 
number between 0 and 10.
"""

import asyncio
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    This is an asynchronous coroutine that takes in no
    arguments. The coroutine will loop 10 times, each
    time asynchronously wait 1 second, then yield a
    random number between 0 and 10.
    Returns:
        Random number between 0 and 10.
    """
    result = [i async for i in asyncio.run(async_generator())]
