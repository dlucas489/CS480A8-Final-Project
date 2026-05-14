"""
analytic_noisy.py — Closed-form noisy Grover success probability under uniform amplitude damping.

Derivation
----------
Amplitude damping is applied to every qubit at (2k + 1) distinct layers within a
k-iteration Grover circuit:
  - 1 layer after the initial Hadamard preparation
  - k layers after the oracle sub-layer
  - k layers after the diffuser sub-layer

For a single-qubit amplitude damping channel with parameter gamma, the excited-state
survival factor per application is (1 - gamma).  Across n_qubits qubits and (2k + 1)
layers, the success-state amplitude envelope picks up a factor
(1 - gamma)^(n_qubits * (2k + 1) / 2), so the probability (amplitude squared) acquires

    damping_factor = (1 - gamma)^(n_qubits * (2k + 1))

The noiseless Grover success probability is sin^2((2k + 1) * theta) where
theta = arcsin(1 / sqrt(N)), giving:

    P(k, N, gamma) = (1 - gamma)^(n_qubits * (2k + 1)) * sin^2((2k + 1) * theta)
"""

import math


def noisy_success_probability(N: int, k: int, gamma: float) -> float:
    """Return the analytic noisy Grover success probability under uniform amplitude damping.

    Parameters
    ----------
    N : int
        Search space size. Must be a power of 2 and >= 2.
    k : int
        Number of Grover iterations. k=0 gives the post-Hadamard state with no oracle calls.
    gamma : float
        Single-application amplitude damping parameter in [0, 1).

    Returns
    -------
    float
        P = (1 - gamma)^(n_qubits * (2k + 1)) * sin^2((2k + 1) * arcsin(1 / sqrt(N)))
    """
    if N < 2:
        raise ValueError(f"N must be >= 2, got {N}")
    if k < 0:
        raise ValueError(f"k must be >= 0, got {k}")
    if not (0.0 <= gamma < 1.0):
        raise ValueError(f"gamma must be in [0, 1), got {gamma}")
    n_qubits = int(round(math.log2(N)))
    theta = math.asin(1.0 / math.sqrt(N))
    layers = 2 * k + 1
    damping = (1.0 - gamma) ** (n_qubits * layers)
    return damping * math.sin(layers * theta) ** 2
