# Grover's Algorithm Under Amplitude Damping: A Cross-Platform Analysis

**CS 480 — Final Project**

## Overview

This project investigates **Grover's Algorithm** under the effect of **amplitude damping (qubit decay)**, quantifying how T₁ relaxation degrades search efficacy across four distinct quantum hardware architectures:

| Platform | Technology |
|---|---|
| IBM Quantum | Superconducting qubits |
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
