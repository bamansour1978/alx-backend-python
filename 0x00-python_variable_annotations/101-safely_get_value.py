#!/usr/bin/env python3
"""Module documentation"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """Function documentation """
    if key in dct:
        return dct[key]
    else:
        return default
