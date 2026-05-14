# Grover's Algorithm Under Amplitude Damping: A Cross-Platform Analysis

**CS 480 — Final Project**

This project quantifies how $T_1$ relaxation (amplitude damping) degrades Grover's algorithm across four quantum hardware platforms, and evaluates whether the $T_1/t_\text{gate}$ ratio predicts Grover search fidelity.

## Research Questions

- **Q1**: How does qubit decay suppress Grover's success probability as a function of circuit depth, and does the suppression rate scale with $N$?
- **Q2**: At what circuit depth does each platform's Grover search lose its quantum advantage over classical random guessing, for varying $N$?
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
│       └── amplitude_damping.py  # gamma_from_specs
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

Noisy Grover circuits use `qml.device("default.mixed")`. `qml.AmplitudeDamping(gamma, wires=i)` is applied to every qubit after the initial Hadamard layer and after each oracle and diffuser sub-layer. The quantum advantage threshold is the first iteration $k$ at which $P(\text{success}) < 1/N$.

Large-N results ($N \geq 64$) use a closed-form analytic model validated against PennyLane simulations at $N \in \{4, 8, 16, 32\}$: $P(k, N, \gamma) = (1-\gamma)^{n \cdot (2k+1)} \cdot \sin^2\!\bigl((2k+1)\theta\bigr)$.

## Data Sources

- IBM: Kim et al., *Nature* 618, 500–505 (2023)
- Google: Arute et al., *Nature* 574, 505–510 (2019)
- Intel: Zwerver et al., *Nature Electronics* 5, 184–190 (2022)
- IonQ: Wright et al., *Nature Communications* 10, 5464 (2019)
