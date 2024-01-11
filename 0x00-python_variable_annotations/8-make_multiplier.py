#!/usr/bin/env python3
"""Module documentation"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function 1 documentation"""
    def multiplier_func(number: float) -> float:
        """function 2 documentation"""
        return number * multiplier
    return multiplier_func
