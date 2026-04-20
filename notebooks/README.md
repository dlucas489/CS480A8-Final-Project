# notebooks/

Jupyter notebooks for exploratory analysis and figure generation.

## Planned Notebooks

| Notebook | Purpose |
|---|---|
| `01_hardware_specs.ipynb` | Survey and verify published T₁/t_gate values; compute γ per platform |
| `02_grover_ideal.ipynb` | Visualize ideal (noiseless) Grover success probability vs. iterations |
| `03_amplitude_damping.ipynb` | Explore amplitude damping model; validate γ derivation |
| `04_cross_platform_simulation.ipynb` | Full noisy Grover simulation across all four platforms and N values |
| `05_threshold_analysis.ipynb` | Identify crossover depth where Grover loses classical advantage |
| `06_figures.ipynb` | Generate all publication-ready figures |

## Running Notebooks

```bash
# From the repository root (with .venv activated):
jupyter notebook notebooks/
```
