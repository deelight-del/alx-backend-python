#!/usr/bin/env python3
"""Module that implements Basic Annotations and
function annotation completion"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Function implementation of safe_first_element"""
    if lst:
        return lst[0]
    else:
        return None
