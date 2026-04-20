# tests/

Unit tests for the simulation codebase.

## Planned Test Modules

| File | Tests |
|---|---|
| `test_noise.py` | Verify γ derivation; boundary conditions (T₁ → ∞ gives γ → 0) |
| `test_grover.py` | Circuit output dimensions; oracle marks correct state |
| `test_platforms.py` | All four platform spec dictionaries have required keys |
| `test_analysis.py` | Threshold detection returns valid circuit depth |

## Running Tests

```bash
# From the repository root (with .venv activated):
pytest tests/
```
