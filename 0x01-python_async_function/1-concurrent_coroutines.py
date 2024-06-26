#!/usr/bin/env python3
"""In this module we explore the basics of
the async syntax"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function implementation of wait_n"""
    random_values = await asyncio.gather(
        *[
            wait_random(max_delay)
            for _ in range(n)
        ])
    return sorted(random_values)
