#!/usr/bin/env python3
"""Module that implements Basic Annotations and
function annotation completion"""
from typing import Any, Optional


def safe_first_element(lst: Any) -> Optional[Any]:
    """Function implementation of safe_first_element"""
    if lst:
        return lst[0]
    else:
        return None
