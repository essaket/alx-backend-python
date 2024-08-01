#!/usr/bin/env python3
"""8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A function return a function multiplies a float by multiplier"""
    def multiple(m: float) -> float:
        """A function that multiplies a float by multiplier"""
        return m * multiplier
    return multiple
