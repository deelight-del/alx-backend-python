#!/usr/bin/env python3
"""Module that implements Basic Annotations and
function annotation completion"""
from typing import Any, Sequence, Union, Mapping, TypeVar

T = TypeVar('T')
def safely_get_value(dct: Mapping[Any, T], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """Function implementation of safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
