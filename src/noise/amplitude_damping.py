"""
amplitude_damping.py — Amplitude damping channel helpers.

The amplitude damping channel models T1 (energy relaxation) noise.
It maps |1><1| toward |0><0| with a per-application probability gamma.

Kraus representation
--------------------
K0 = [[1,       0      ],      K1 = [[0, sqrt(gamma)],
      [0, sqrt(1-gamma)]]            [0, 0           ]]

such that K0†K0 + K1†K1 = I  (trace-preserving).

Connection to hardware specs
----------------------------
Given a gate time t_gate and qubit coherence time T1 (same units):

    gamma = 1 - exp(-t_gate / T1)

For t_gate << T1 (typical hardware):  gamma ~ t_gate / T1.
"""

import math
import numpy as np


# ---------------------------------------------------------------------------
# gamma derivation
# ---------------------------------------------------------------------------

def gamma_from_specs(T1_us: float, t_gate_ns: float) -> float:
    """Derive the amplitude damping parameter from hardware specifications.

    Parameters
    ----------
    T1_us : float
        Qubit energy-relaxation time in microseconds.
    t_gate_ns : float
        Representative gate time in nanoseconds.

    Returns
    -------
    float
        gamma = 1 - exp(-t_gate / T1), with both times in nanoseconds.
    """
    if T1_us <= 0:
        raise ValueError(f"T1_us must be positive, got {T1_us}")
    if t_gate_ns <= 0:
        raise ValueError(f"t_gate_ns must be positive, got {t_gate_ns}")
    T1_ns = T1_us * 1_000.0
    return 1.0 - math.exp(-t_gate_ns / T1_ns)


# ---------------------------------------------------------------------------
# Kraus operators
# ---------------------------------------------------------------------------

def kraus_operators(gamma: float) -> tuple:
    """Return the two Kraus operators for the amplitude damping channel.

    Parameters
    ----------
    gamma : float
        Damping probability in [0, 1).

    Returns
    -------
    K0, K1 : tuple of np.ndarray, shape (2, 2), dtype complex128
    """
    if not (0.0 <= gamma < 1.0):
        raise ValueError(f"gamma must be in [0, 1), got {gamma}")
    K0 = np.array([[1.0, 0.0],
                   [0.0, math.sqrt(1.0 - gamma)]], dtype=complex)
    K1 = np.array([[0.0, math.sqrt(gamma)],
                   [0.0, 0.0             ]], dtype=complex)
    return K0, K1


# ---------------------------------------------------------------------------
# Channel application
# ---------------------------------------------------------------------------

def apply_channel(rho: np.ndarray, gamma: float) -> np.ndarray:
    """Apply the amplitude damping channel once: rho -> K0 rho K0† + K1 rho K1†.

    Parameters
    ----------
    rho : np.ndarray, shape (2, 2)
        Single-qubit density matrix.
    gamma : float
        Damping probability.

    Returns
    -------
    np.ndarray, shape (2, 2)
        Output density matrix.
    """
    K0, K1 = kraus_operators(gamma)
    return K0 @ rho @ K0.conj().T + K1 @ rho @ K1.conj().T


def apply_channel_k_times(rho: np.ndarray, gamma: float, k: int) -> np.ndarray:
    """Apply the amplitude damping channel k times sequentially.

    Parameters
    ----------
    rho : np.ndarray, shape (2, 2)
        Initial single-qubit density matrix.
    gamma : float
        Damping probability per application.
    k : int
        Number of channel applications.

    Returns
    -------
    np.ndarray, shape (2, 2)
        Output density matrix after k applications.
    """
    if k < 0:
        raise ValueError(f"k must be >= 0, got {k}")
    result = rho.copy().astype(complex)
    for _ in range(k):
        result = apply_channel(result, gamma)
    return result


# ---------------------------------------------------------------------------
# Analytical closed forms
# ---------------------------------------------------------------------------

def analytical_rho11(rho11_initial: float, gamma: float, k: int) -> float:
    """Closed-form excited-state population after k channel applications.

    Derived from the Kraus map:
        rho11(k) = rho11(0) * (1 - gamma)^k

    Parameters
    ----------
    rho11_initial : float
        Initial excited-state population rho[1, 1].
    gamma : float
        Damping probability per application.
    k : int
        Number of channel applications.

    Returns
    -------
    float
    """
    return rho11_initial * (1.0 - gamma) ** k


def analytical_rho01_magnitude(rho01_initial: complex, gamma: float, k: int) -> float:
    """Closed-form off-diagonal magnitude after k channel applications.

    From the Kraus map:
        |rho01(k)| = |rho01(0)| * sqrt(1 - gamma)^k

    Parameters
    ----------
    rho01_initial : complex
        Initial off-diagonal element rho[0, 1].
    gamma : float
        Damping probability per application.
    k : int
        Number of channel applications.

    Returns
    -------
    float
    """
    return abs(rho01_initial) * (1.0 - gamma) ** (k / 2.0)
