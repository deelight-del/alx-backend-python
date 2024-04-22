#!/usr/bin/env python3
"""In this module we explore the basics of
the async syntax"""


import asyncio
from typing import List
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """The implementation of the measure_time function"""
    current_s = time.perf_counter()
    await wait_n(n, max_delay)
    new_s = time.perf_counter() - current_s
    return new_s/n
