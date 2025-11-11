# The function implements the Leibniz series to approximate the value of pi.
# The series is: pi/4 = 1/1 - 1/3 + 1/5 - 1/7 + ...
def approximate_pi(n_terms: int) -> float:
    """
    Estimates the value of pi using the Leibniz formula for the first n_terms.
    Returns 0.0 if n_terms is less than 1.

    :param n_terms: The number of terms to include in the series (must be >= 1).
    :return: The estimated value of pi.
    """
    # Handles invalid input silently, returning 0.0 instead of raising an error.
    if n_terms < 1:
        return 0.0

    pi_over_four_sum = 0.0

    # The loop iterates from n = 0 up to n = n_terms - 1.
    for n in range(n_terms):
        # Calculate the denominator: (2 * n) + 1, which generates 1, 3, 5, 7, ...
        denominator = 2 * n + 1

        # Calculate the numerator's sign: (-1)^n.
        # If n is even (0, 2, 4...), sign is +1.
        # If n is odd (1, 3, 5...), sign is -1.
        if n % 2 == 0:
            term = 1.0 / denominator
        else:
            term = -1.0 / denominator

        pi_over_four_sum += term

    # Since the series approximates pi/4, we multiply the final sum by 4.
    estimated_pi = pi_over_four_sum * 4
    return estimated_pi
