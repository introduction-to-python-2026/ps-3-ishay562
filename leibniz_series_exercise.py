def approximate_pi(n_terms):
    leibniz_series = []
    for i in range(n_terms):
        term = ((-1)**i) / (2 * i + 1)
        leibniz_series.append(term)

    sum_leibniz = sum(leibniz_series)
    approx_pi = 4 * sum_leibniz
    return approx_pi
