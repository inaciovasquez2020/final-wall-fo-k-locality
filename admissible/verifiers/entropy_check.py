import math

def check_entropy_step(alphabet_size, It):
    """
    Verifies ΔH ≤ I_t using worst-case entropy bound.
    """
    delta_H = math.log2(alphabet_size + 1)
    return delta_H <= It

def verify_trace(trace, alphabet_size):
    for step in trace:
        if not check_entropy_step(alphabet_size, step["I"]):
            return False, step["t"]
    return True, None

