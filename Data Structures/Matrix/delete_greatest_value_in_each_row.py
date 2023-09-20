grid = [[1, 2, 4],
        [3, 3, 1]]

length = len(grid)
result = 0

while True:

    if len(grid[0]) == 0:
        break

    current_max = []

    for row in range(length):
        max_element = max(grid[row])

        grid[row].remove(max_element)
        current_max.append(max_element)

    result = result + max(current_max)

print(result)
