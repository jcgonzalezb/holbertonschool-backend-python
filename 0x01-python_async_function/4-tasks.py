#!/usr/bin/env python3
"""
This project module contains an asynchronous coroutine that
takes in two integer arguments and returns a list of random
delays printed a number of times. The list should be in
ascending order.
"""

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """
    This is an asynchronous coroutine that takes in two
    integer arguments (n and max_delay) and returns a list
    list of all the delays (float values). The number of
    delays is the same as n. The list should be in
    ascending order without using sort().
    Returns:
        A list of all the delays (float values).
    """
    wait_list = []

    for i in range(0, n):
        wait_list.append(await task_wait_random(max_delay))
        i += 1

    return sorted(wait_list)
