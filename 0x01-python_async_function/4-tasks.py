#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function waits for a random delay between 0 and max_delay n times"""
    # Create a list of wait_random coroutines
    listdelay = [task_wait_random(max_delay) for _ in range(n)]
    # Run all the coroutines concurrently and wait for them to complete
    delays = await asyncio.gather(*listdelay)
    # Return the sorted list of delays
    return sorted(delays)
