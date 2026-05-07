"""
success.py — Success probability sweep utilities.
"""

from typing import Optional

import numpy as np
from grover.grover import ideal_success_probability, optimal_iterations


def sweep_iterations(N: int, k_max: Optional[int] = None):
    """Compute ideal Grover success probability for k = 0 … k_max.

    Parameters
    ----------
    N : int
        Search space size.
    k_max : int, optional
        Maximum iteration count. Defaults to 2 × optimal_iterations(N) so the
        oscillatory overshoot past the peak is visible.

    Returns
    -------
    ks : np.ndarray of int
        Iteration indices [0, 1, …, k_max].
    probs : np.ndarray of float
        Corresponding ideal success probabilities.
    """
    if k_max is None:
        k_max = 2 * optimal_iterations(N)
    ks = np.arange(0, k_max + 1, dtype=int)
    probs = np.array([ideal_success_probability(N, int(k)) for k in ks])
    return ks, probs
