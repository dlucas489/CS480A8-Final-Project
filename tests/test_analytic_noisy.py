import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from noise.analytic_noisy import noisy_success_probability
from grover.grover import optimal_iterations, ideal_success_probability


def test_k0_gamma0_uniform_superposition():
    # at k=0 with no noise, P = sin^2(arcsin(1/sqrt(N))) = 1/N
    for N in [4, 8, 16, 32, 64]:
        p = noisy_success_probability(N, k=0, gamma=0.0)
        assert abs(p - 1.0 / N) < 1e-12, f"N={N}: expected {1/N}, got {p}"


def test_kopt_gamma0_matches_ideal():
    # with no noise the damping factor is 1, so result must equal ideal
    for N in [4, 8, 16, 32, 64]:
        k_opt = optimal_iterations(N)
        p_noisy = noisy_success_probability(N, k=k_opt, gamma=0.0)
        p_ideal = ideal_success_probability(N, k_opt)
        assert abs(p_noisy - p_ideal) < 1e-12, (
            f"N={N}, k_opt={k_opt}: noisy(gamma=0)={p_noisy}, ideal={p_ideal}"
        )


def test_monotone_decrease_beyond_kopt():
    # immediately after k_opt, sin^2 is descending from its peak; combined with
    # the monotonically shrinking damping envelope, P must be strictly decreasing
    # for the next several iterations (checked over a range where sin^2 has not
    # yet started its second rise)
    N, gamma = 64, 0.001
    k_opt = optimal_iterations(N)
    probs = [noisy_success_probability(N, k, gamma) for k in range(k_opt, k_opt + 5)]
    for i in range(len(probs) - 1):
        assert probs[i] > probs[i + 1], (
            f"N={N}, gamma={gamma}: P not decreasing at k={k_opt + i} -> {k_opt + i + 1}"
        )
