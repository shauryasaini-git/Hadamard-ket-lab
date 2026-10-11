import numpy as np

ket_zero = np.array([1, 0])
H_gate = (1 / (2 ** 0.5)) * np.array([[1, 1], [1, -1]])

def apply_gate(gate, state_vector):
    return gate @ state_vector

def calculate_probability(state_vector):
    prob_zero = np.square(abs(state_vector[0]))
    prob_one = np.square(abs(state_vector[1]))
    return prob_zero, prob_one

def measure(state_vector):
    prob_zero, prob_one = calculate_probability(state_vector)
    options = [0, 1]
    result =  np.random.choice(options, p = [prob_zero, prob_one])
    return result

def main():
    print("Intializing qubit to ket zero")
    current_state = ket_zero

    print("Applying H gate")
    current_state = apply_gate(H_gate, current_state)

    print("Calculating probabilities")
    p0, p1 = calculate_probability(current_state)
    print("Odds of getting 0:" ,p0, "Odds of getting 1:", p1)

    print("Meauring qubit")
    final_result = measure(current_state)
    print("Measured outcome:", final_result)

if __name__ == "__main__":
    main()