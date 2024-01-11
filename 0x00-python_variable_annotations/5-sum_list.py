#!/usr/bin/env python3
"""Sum of flot's list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Sum of flot's list"""
    if input_list is None:
        return 0.0
    else:
        return sum(input_list)
