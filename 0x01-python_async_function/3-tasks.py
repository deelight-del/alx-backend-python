#!/usr/bin/env python3
"""In this module we explore the basics of
the async syntax"""


import asyncio
from typing import List
import time


wait_random = __import__('0-baic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function implementation of task_wait_random funciton"""
    return asyncio.create_task(max_delay)
