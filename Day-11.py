matrix = []
for _ in range(6):
    row = list(map(int, input().split()))
    matrix.append(row)

max_sum = float("-inf")
for i in range(4):
    for j in range(4):
        sum_hourglass = (matrix[i][j] + matrix[i][j+1] + matrix[i][j+2]) + (matrix[i+1][j+1]) + (matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2])

        if sum_hourglass > max_sum:
            max_sum = sum_hourglass

print(max_sum)
