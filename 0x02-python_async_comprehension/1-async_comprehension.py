#!/usr/bin/env python3
"""The implementation and use of async_genrator"""


from typing import List


async_genrator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Funciton implementation of async_comprehension"""
    return [i async for i in async_genrator()]
