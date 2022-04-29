#!/usr/bin/env python3
"""
This project module contains an asynchronous coroutine
"""

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Returns a list of all the delays (float values).
    """
    wait_list = []

    for i in range(n):
        wait_list.append(await task_wait_random(max_delay))

    return sorted(wait_list)
