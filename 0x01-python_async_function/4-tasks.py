#!/usr/bin/env python3
"""In this module we explore the basics of
the async syntax"""


import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function implementation of wait_n"""
    results = [await task_wait_random(max_delay) for _ in range(n)]
    return sorted(results)
