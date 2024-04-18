#!/usr/bin/env python3
"""Module that implements Basic Annotations and
function definition of make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Defining the mulitpilier function"""
    def multiplierFunc(const: float) -> float:
        """Defining the multiplierFunc"""
        return const * multiplier
    return multiplierFunc
