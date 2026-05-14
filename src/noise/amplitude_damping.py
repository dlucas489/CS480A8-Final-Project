"""Given a hardware relaxation time T1 (in microseconds) and gate time t_gate (in nanoseconds), returns the amplitude damping probability gamma = 1 - exp(-t_gate / (T1 * 1000))."""
"""Given a hardware relaxation time T1 (in microseconds) and gate time t_gate (in nanoseconds), returns the amplitude damping probability gamma = 1 - exp(-t_gate / (T1 * 1000))."""

import math


def gamma_from_specs(T1_us: float, t_gate_ns: float) -> float:
    """Return gamma = 1 - exp(-t_gate_ns / (T1_us * 1000))."""
    T1_ns = T1_us * 1_000.0
    return 1.0 - math.exp(-t_gate_ns / T1_ns)

