#!/usr/bin/env python3
"""An asynchronous coroutine"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ return the list of all the delays
        spawned from wait_random in asc order
        for n times
    """
    list = []
    for _ in range(n):
        wait_times = await wait_random(max_delay)
        list.append(wait_times)
    return sorted(list)
