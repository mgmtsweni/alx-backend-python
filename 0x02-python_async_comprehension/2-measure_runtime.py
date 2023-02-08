#!/usr/bin/env python3

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """measure the total runtime and return it."""
    start_time = time.time()
    measure = [async_comprehension() for i in range(4)]
    await asyncio.gather(*measure)
    end_time = time.time()
    return (end_time - start_time)