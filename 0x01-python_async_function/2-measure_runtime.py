#!/usr/bin/env python3
"""
This project module contains an asynchronous coroutine that
takes in two integer arguments and returns a list of random
delays printed a number of times. The list should be in
ascending order.
"""

import time

wait_n = __import__('2-measure_runtime').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    This is an asynchronous coroutine that takes in two
    integer arguments (n and max_delay) and returns a list
    list of all the delays (float values). The number of
    delays is the same as n. The list should be in
    ascending order without using sort().
    Returns:
        A list of all the delays (float values).
    """
    begin = time.time()
    wait_n(n, max_delay)
    end = time.time()

    total_time = end - begin

    return (total_time / n)
