# Import the function from the existing file for clarity
from move_item import move 

# Scenario 1: Pig is at the far right and attempts to move right.
list_at_right_boundary = [0, 0, 0, 1]
direction_right = 'right'

# Calculate the result
result_right = move(list_at_right_boundary, direction_right)

# Expected Outcome
# The condition 'index_of_one < len(my_list) - 1' (3 < 4 - 1, or 3 < 3) is False.
# The list should remain unchanged.
expected_right = [0, 0, 0, 1]

# Scenario 2: Pig is at the far left and attempts to move left.
list_at_left_boundary = [1, 0, 0, 0]
direction_left = 'left'

# Calculate the result
result_left = move(list_at_left_boundary, direction_left)

# Expected Outcome
# The condition 'index_of_one > 0' (0 > 0) is False.
# The list should remain unchanged.
expected_left = [1, 0, 0, 0]

# Description of the Edge Case Behavior:
"""
The edge case occurs when the pig (1) is at a boundary position (index 0 or index N-1) 
and is commanded to move off the list.

The function successfully handles this by:
1.  **Right Boundary:** The check 'index_of_one < len(my_list) - 1' is False when the pig is at the last position.
2.  **Left Boundary:** The check 'index_of_one > 0' is False when the pig is at the first position.

In both cases, the movement block is skipped, and the original list is returned without change, preventing an IndexError.
"""
