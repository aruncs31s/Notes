list_of_lists_of_lists = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],  # First level  # Second level
    [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],  # First level  # Second level
]

# Accessing elements
print(list_of_lists_of_lists[0][1][2])  # Accessing '6'
print(list_of_lists_of_lists[1][2][0])  # Accessing 'g'
