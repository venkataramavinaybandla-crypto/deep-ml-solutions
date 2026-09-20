def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	# Your code here

	T = []

	for i in matrix:
		tr = []
		for r in i:
			tr.append(r*scalar)
		T.append(tr)

	return T