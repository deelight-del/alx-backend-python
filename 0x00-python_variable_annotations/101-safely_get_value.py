#!/usr/bin/env python3
"""Module that implements Basic Annotations and
function annotation completion"""
from typing import Sequence, Union, Mapping, TypeVar, Any

T = TypeVar('T')
def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[~T, None] = None) -> Union[Any, ~T]:
    """Function implementation of safely_get_value"""
    if key in dct:
        return dct[key]
    else:
        return default
