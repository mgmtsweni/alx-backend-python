#!/usr/bin/env python3
"""A type-annotated function"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    return float(sum(mxd_list))
