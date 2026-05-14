# Grover's Algorithm Under Amplitude Damping: A Cross-Platform Analysis

**CS 480 — Final Project**

This project quantifies how $T_1$ relaxation (amplitude damping) degrades Grover's algorithm across four quantum hardware platforms, and evaluates whether the $T_1/t_\text{gate}$ ratio predicts Grover search fidelity.

## Research Questions

- **Q1**: How does qubit decay suppress Grover's success probability as a function of circuit depth, and does the suppression rate scale with $N$?
- **Q2**: How does noise-induced fidelity degradation at $k_\text{opt}$ scale with search space size $N$, and at what scale does each platform's advantage become substantially impaired?
- **Q3**: Can the $T_1/t_\text{gate}$ ratio alone rank the four platforms by Grover search fidelity?

## Hardware Platforms

| Platform | Technology | $T_1$ | $t_\text{gate}$ |
|---|---|---|---|
| IBM Quantum Eagle | Superconducting | 100 µs | 50 ns |
| Google Sycamore | Superconducting | 15 µs | 12 ns |
| Intel Tunnel Falls | Spin qubit | 1,000 µs | 1,000 ns |
| IonQ Aria | Trapped ion | 10,000,000 µs | 135,000 ns |

## File Structure

```
CS480A8-Final-Project/
├── src/
│   ├── grover/
│   │   └── grover.py          # optimal_iterations, ideal_success_probability
│   └── noise/
│       ├── amplitude_damping.py  # gamma_from_specs
│       └── analytic_noisy.py     # noisy_success_probability
├── data/
│   ├── hardware_specs/
│   │   └── hardware_specs.csv
│   └── results/
│       └── thresholds.csv     # written by notebook 02
├── results/
│   └── figures/               # PNGs written by notebooks
├── notebooks/
│   ├── 01_grover_ideal.ipynb
│   ├── 02_noisy_simulation.ipynb
│   └── 03_platform_comparison.ipynb
├── requirements.txt
├── README.md
├── LICENSE.md
└── .gitignore
```

## Setup

```bash
pip install -r requirements.txt
```

## Running

Execute notebooks in order:

1. `01_grover_ideal.ipynb` — noiseless PennyLane simulation; cross-validates against analytic formula
2. `02_noisy_simulation.ipynb` — amplitude-damped simulation; writes `data/results/thresholds.csv`
3. `03_platform_comparison.ipynb` — loads thresholds; produces scatter and bar plots; answers Q1–Q3

All figures are saved to `results/figures/`.

## Methodology

The amplitude damping channel parameter is derived from hardware specifications:

$$\gamma = 1 - \exp\!\left(-\frac{t_\text{gate}}{T_1 \times 1000}\right)$$

Noisy Grover circuits use `qml.device("default.mixed")`. `qml.AmplitudeDamping(gamma, wires=i)` is applied to every qubit after the initial Hadamard layer and after each oracle and diffuser sub-layer.

Notebook 02 sweeps $N \in \{4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192\}$ (all powers of 2 from $2^2$ to $2^{13}$). The small-N tier ($N \leq 32$) uses PennyLane `default.mixed` exact simulation to validate the analytic model; the large-N tier ($N \geq 64$) uses the closed-form analytic model exclusively, as density-matrix simulation becomes computationally prohibitive.

The analytic model: $P(k, N, \gamma) = (1-\gamma)^{n \cdot (2k+1)} \cdot \sin^2\!\bigl((2k+1)\theta\bigr)$. The primary Q2 metric is the fidelity ratio $P_\text{noisy}(k_\text{opt}) / P_\text{ideal}(k_\text{opt})$, which isolates noise-induced degradation from the algorithm's oscillation structure.

## Data Sources

- IBM: Kim et al., *Nature* 618, 500–505 (2023)
- Google: Arute et al., *Nature* 574, 505–510 (2019)
- Intel: Zwerver et al., *Nature Electronics* 5, 184–190 (2022)
- IonQ: Wright et al., *Nature Communications* 10, 5464 (2019)
