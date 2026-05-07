"""
grover.py — Analytic Grover circuit helpers (noiseless).

Formulae
--------
Success probability after k Grover iterations on a search space of N items
with exactly 1 marked item:

    P(k) = sin²( (2k + 1) · θ )    where  θ = arcsin(1 / √N)

Optimal iteration count:

    k_opt = floor( π / (4θ) )  ≈  floor( (π/4) · √N )
"""

import math
import numpy as np


def _theta(N: int) -> float:
    """Half-angle for Grover rotation: arcsin(1/√N)."""
    return math.asin(1.0 / math.sqrt(N))


def optimal_iterations(N: int) -> int:
    """Return the optimal number of Grover iterations for search space size N.

    Parameters
    ----------
    N : int
        Search space size. Must be a power of 2 and >= 2.

    Returns
    -------
    int
        k_opt = floor( π / (4 · arcsin(1/√N)) )
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    return int(math.floor(math.pi / (4.0 * _theta(N))))


def ideal_success_probability(N: int, k: int) -> float:
    """Return the exact noiseless Grover success probability after k iterations.

    Parameters
    ----------
    N : int
        Search space size.
    k : int
        Number of Grover iterations (k=0 → uniform superposition, no oracle calls).

    Returns
    -------
    float
        P = sin²( (2k + 1) · arcsin(1/√N) )
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    if k < 0:
        raise ValueError(f"k must be >= 0, got {k}")
    theta = _theta(N)
    return math.sin((2 * k + 1) * theta) ** 2
