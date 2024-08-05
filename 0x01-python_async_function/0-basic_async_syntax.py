#!/usr/bin/env python3
"""0. The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
        """A function return a a random delay"""
        delay = random.uniform(0, max_delay) # Generate a random delay between 0 and max_delay
        await asyncio.sleep(delay) # wait for random delay
        return delay # return the delay
