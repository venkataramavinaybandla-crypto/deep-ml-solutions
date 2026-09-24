def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
    n = len(vectors[0])

    means = []
    for vector in vectors:
        means.append(sum(vector) / n)

    covariance_matrix = []

    for i in range(len(vectors)):
        row = []

        for j in range(len(vectors)):
            covariance = 0

            for k in range(n):
                covariance += (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])

            covariance /= (n - 1)
            row.append(covariance)

        covariance_matrix.append(row)

    return covariance_matrix