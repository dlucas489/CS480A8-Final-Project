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

## Data Sources

- IBM: Kim et al., *Nature* 618, 500–505 (2023)
- Google: Arute et al., *Nature* 574, 505–510 (2019)
- Intel: Zwerver et al., *Nature Electronics* 5, 184–190 (2022)
- IonQ: Wright et al., *Nature Communications* 10, 5464 (2019)

| Google Quantum AI | Superconducting qubits |
| Intel Tunnel Falls | Silicon spin qubits |
| IonQ Aria | Trapped ion qubits |

Under ideal conditions, Grover's Algorithm achieves a quadratic speedup over classical probabilistic search — requiring O(√N) oracle queries to find a marked item in an unsorted database of N entries. This project measures how qubit decay (amplitude damping) exponentially suppresses that advantage as a function of circuit depth, and whether a platform's **T₁/t_gate ratio** serves as a reliable discriminator for Grover fidelity.

---

## Research Questions

**Q1 — Decay vs. Circuit Depth:**  
How does qubit decay suppress Grover's success probability as a function of circuit depth, and does the suppression rate scale with search space size (N)?

**Q2 — Cross-Platform Threshold Analysis:**  
Given published T₁ and t_gate values, at what circuit depth does each platform's Grover search lose its quantum advantage over classical random guessing, for varying N?

**Q3 — T₁/t_gate as a Fidelity Predictor:**  
Can the T₁/t_gate ratio alone rank the four platforms by Grover search fidelity?

---

## Methodology

- **Simulator:** PennyLane `default.mixed` device
- **Noise model:** `qml.AmplitudeDamping` applied after each gate layer; all other noise channels held at zero
- **Damping parameter:** γ derived from published hardware specs via γ = 1 − exp(−t_gate / T₁)
- **Search space sizes (N):** Powers of 2 up to N = 256 (3–8 qubits)
- **Shots per experiment:** 8192 (for stable success-probability estimates)

---

## Repository Structure

```
CS480A8-Final-Project/
├── src/
│   ├── grover/          # Grover circuit construction
│   ├── noise/           # Amplitude damping noise channel helpers
│   ├── platforms/       # Published hardware specs (T₁, t_gate) per platform
│   └── analysis/        # Success probability computation & threshold detection
├── data/
│   ├── hardware_specs/  # Raw / cited hardware parameter tables
│   └── results/         # Simulation output (CSV / JSON)
├── notebooks/           # Jupyter notebooks for exploration and figure generation
├── results/
│   └── figures/         # Final publication-ready plots
├── tests/               # Unit tests
└── docs/                # Additional documentation and references
```

---

## Setup

### Prerequisites

- Python ≥ 3.10
- [PennyLane](https://pennylane.ai/) and its dependencies

### Installation

```bash
# Clone the repository
git clone https://github.com/dlucas489/CS480A8-Final-Project.git
cd CS480A8-Final-Project

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running Simulations

```bash
# (instructions to be added as implementation progresses)
```

---

## Hardware Parameters

| Platform | T₁ (µs) | t_gate (ns) | T₁/t_gate |
|---|---|---|---|
| IBM Quantum (Eagle) | ~100 | ~50 | ~2,000 |
| Google Quantum AI (Sycamore) | ~15 | ~12 | ~1,250 |
| Intel Tunnel Falls (spin) | ~1,000 | ~1,000 | ~1,000 |
| IonQ Aria (trapped ion) | ~10,000,000 | ~135,000 | ~74,000 |

*Values are representative estimates from published literature; exact citations in `docs/references.md`.*

---

## License

This project is licensed under the MIT License — see [LICENSE.md](LICENSE.md) for details.

---

## Author

**dlucas489** — CS 480, Spring 2026
