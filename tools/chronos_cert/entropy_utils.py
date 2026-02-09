import math
from typing import List

TOL = 1e-12

def normalize(p: List[float]) -> List[float]:
    s = sum(p)
    if s <= 0:
        raise ValueError("probability sum must be positive")
    return [x / s for x in p]

def entropy_bits(p: List[float]) -> float:
    h = 0.0
    for x in p:
        if x < -TOL:
            raise ValueError("negative probability")
        if x <= 0.0:
            continue
        h -= x * math.log2(x)
    return h

def entropy_drop(p_prev: List[float], p_next: List[float]) -> float:
    return entropy_bits(p_prev) - entropy_bits(p_next)
