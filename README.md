[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/aSH8JZL6)
# Python Exercises: Edge Cases and Approximate π

## Overview
This assignment consists of two exercises designed to help you understand lists and loops in Python. You will be required to modify two Python files: `edge_case_exercise.py` and `leibniz_series_exercise.py`.

---

## Problem 1: Handling Edge Cases
### File: `edge_case_exercise.py`

You are given a function `move()` that simulates the movement of a pig (represented by `1`) across a list of zeros. The function takes two parameters:
1. **`my_list`**: A list of zeros with one `1`, indicating the pig's current position.
2. **`direction`**: A string (`'left'` or `'right'`) specifying the direction of movement.

The function should:
- Move the `1` to the left or right.
- Handle edge cases where moving the `1` would push it out of the list by leaving it in its current position.

### Example:
```python
move([0, 0, 0, 1, 0], 'right')  # Output: [0, 0, 0, 0, 1]
move([0, 1, 0, 0, 0], 'left')   # Output: [1, 0, 0, 0, 0]
move([1, 0, 0, 0, 0], 'left')   # Output: [1, 0, 0, 0, 0]
```

## Problem 2: Approximate π Using the Leibniz Series
### File: `leibniz_series_exercise.py`

## Overview
In this assignment, you will implement a function to approximate the value of π using the Leibniz series. The Leibniz series is a well-known infinite series that can be used to approximate π.

The formula for the Leibniz series is:
$$\pi = 4 \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1}$$

The task is to create a Python function that approximates π using the first `n_terms` terms of the series.
You need to implement a function `approximate_pi(n_terms)` that approximates the value of π based on the first `n_terms` terms of the Leibniz series.
The function takes one parameter:
-  An integer `n_terms` representing the number of terms to use in the series.

The function return one value:
- A floating-point number that is the approximation of π based on the first `n_terms` terms of the Leibniz series.

### Example:
```python
approximate_pi(10)  # Output: ~3.0418396189
approximate_pi(100)  # Output: ~3.1315929036
approximate_pi(1000)  # Output: ~3.1405926538
```


---

For additional guidance, refer to the accompanying Jupyter Notebook (.ipynb) files, which provide step-by-step instructions and examples to help you complete the tasks.
