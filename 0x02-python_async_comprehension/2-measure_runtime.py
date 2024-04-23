#!/usr/bin/env python3
"""The implementation and use of async comprehension"""


from typing import List
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function to measure runtime of coroutine"""
    first_s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    final_s = time.perf_counter() - first_s
    return final_s
