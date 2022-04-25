#!/usr/bin/env python3
"""
This project module contains an asynchronous coroutine that
takes in two integer arguments and returns a list of random
delays printed a number of times. The list should be in
ascending order.
"""

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> float:
    """
    This is an asynchronous coroutine that takes in two
    integer arguments (n and max_delay) and returns a list
    list of all the delays (float values). The number of
    delays is the same as n. The list should be in ascending order
    without using sort() because of concurrency.
    Returns:
        A list of all the delays (float values).
    """
    wait_list = []

    for i in range(0, n):
        wait_list.append(await wait_random(max_delay))
        i += 1

    sorted_list = sorted(wait_list)

    return sorted_list
