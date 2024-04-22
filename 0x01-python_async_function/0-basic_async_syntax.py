#!/usr/bin/env python3
"""In this module we explore the basics of
the async syntax"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    random_delay = random.uniform(0, max_delay)
    asyncio.asleep(random_delay)
    return(random_delay)
