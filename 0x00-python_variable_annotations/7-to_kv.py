#!/usr/bin/env python3
"""Module that implements Basic Annotations and
function definition of to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Funciton implementation of to_kv funciton"""
    return (k, v**2)
