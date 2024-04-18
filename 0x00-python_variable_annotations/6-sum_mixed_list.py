#!/usr/bin/env python3
"""Module that implements Basic Annotations and
function definition of sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Funciton implementation of sum_mixed_list"""
    return sum(mxd_lst)
