def calculate_matrix_mean(matrix: list[list[int | float]], mode: str) -> list[float]:
    result = []

    if mode == "row":
        for row in matrix:
            mean = sum(row) / len(row)
            result.append(mean)

    elif mode == "column":
        for j in range(len(matrix[0])):
            total = 0

            for i in range(len(matrix)):
                total += matrix[i][j]

            mean = total / len(matrix)
            result.append(mean)

    return result