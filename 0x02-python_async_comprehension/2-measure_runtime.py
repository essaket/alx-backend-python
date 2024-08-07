#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """A fucnton return the total runtime"""
    start = time.time()  # Record the start time
    # Execute four instance of async_comprehension
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    end = time.time()  # Record the end time
    return end - start  # Return the total runtime
