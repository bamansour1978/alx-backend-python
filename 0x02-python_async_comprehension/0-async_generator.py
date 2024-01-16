#!/usr/bin/env python3
"""Module documentation"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function documentation"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
