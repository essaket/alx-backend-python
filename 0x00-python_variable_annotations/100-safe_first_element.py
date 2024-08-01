#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """A function returns the first element of the sequence if it is not empty,
    otherwise, returns None"""
    if lst:
        return lst[0]
    else:
        return None
