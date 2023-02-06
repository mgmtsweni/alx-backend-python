#!/usr/bin/env python3
"""An asynchronous coroutine"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays
        spawned from wait_random in asc order
        for n times
    """
    list = []
    for _ in range(n):
        wait_times = await task_wait_random(max_delay)
        list.append(wait_times)
    return sorted(list)
