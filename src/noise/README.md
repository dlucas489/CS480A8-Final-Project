# src/noise/

Amplitude damping noise channel helpers.

Planned modules:
- `amplitude_damping.py` — compute γ = 1 − exp(−t_gate / T₁) from hardware specs
                           and wrap `qml.AmplitudeDamping` for insertion after each gate layer
