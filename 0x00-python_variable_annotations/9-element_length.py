#!/usr/bin/env python3
"""Module that implements Basic Annotations and
function definition of element_length"""
from typing import Sequence, Iterable, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function implementation of element_length"""
    return [(i, len(i)) for i in lst]
