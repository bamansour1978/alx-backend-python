#!/usr/bin/env python3
"""Module documentation"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Function documentation"""
    return [(i, len(i)) for i in lst]
