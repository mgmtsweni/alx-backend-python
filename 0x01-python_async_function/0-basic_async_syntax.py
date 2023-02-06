#!/usr/bin/env python3
"""An asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay=10):
    """ Takes in an integer argument that waits for a random delay
        and returns it.
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)

    return random_delay
