# Quantum

A minimal single-qubit simulator in Python. It puts a qubit into superposition with a Hadamard gate, computes the measurement probabilities, and simulates a measurement.

## Requirements

- Python 3
- NumPy

```
pip install numpy
```

## Usage

```
python quantum.py
```

Example output:

```
Intializing qubit to ket zero
Applying H gate
Calculating probabilities
Odds of getting 0: 0.4999999999999999 Odds of getting 1: 0.4999999999999999
Meauring qubit
Measured outcome: 1
```

The measured outcome is random: 0 or 1, each about half the time. The probabilities print as `0.4999999999999999` rather than `0.5` because of floating-point rounding.

## How it works

The qubit's state is a 2-element vector of amplitudes, and a gate is a 2×2 matrix.

1. **Initialize.** The qubit starts in the state |0⟩, represented as `[1, 0]`.
2. **Apply the Hadamard gate.** Multiplying the state by the H matrix gives `[1/√2, 1/√2]`, an equal superposition of |0⟩ and |1⟩.
3. **Calculate probabilities.** The probability of each outcome is the squared magnitude of its amplitude (the Born rule), so each is 1/2.
4. **Measure.** One outcome is drawn at random using those probabilities.

## Functions

| Function | Description |
| --- | --- |
| `apply_gate(gate, state_vector)` | Returns the state after applying a gate (matrix-vector product). |
| `calculate_probability(state_vector)` | Returns the probabilities of measuring 0 and 1. |
| `measure(state_vector)` | Simulates a measurement and returns 0 or 1. |

`ket_zero` and `H_gate` are defined as module-level constants.

## Extending it

To try other gates, define them as 2×2 NumPy arrays and pass them to `apply_gate`. For example, the Pauli-X (NOT) gate:

```python
X_gate = np.array([[0, 1], [1, 0]])
state = apply_gate(X_gate, ket_zero)  # [0, 1], always measures 1
```
