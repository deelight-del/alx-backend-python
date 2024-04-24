#!/usr/bin/env python3
"""The implementation and use of async_genrator"""


import random
from typing import AsyncGenerator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """implementation of the async_genrator function"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
