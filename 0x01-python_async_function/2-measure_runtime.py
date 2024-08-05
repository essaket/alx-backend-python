#!/usr/bin/env python3
"""2. Measure the runtime"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    start = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the wait_n function
    end = time.time()  # Record the end time
    return (end - start) / n  # Calculate and retun the total_time
