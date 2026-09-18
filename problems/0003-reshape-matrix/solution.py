import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	lis_len = len(a) * len(a[0])
	new_len = new_shape[0] * new_shape[1]

	if lis_len != new_len:
		return []
	
	reshaped_matrix = np.array(a)
	reshaped_matrix = reshaped_matrix.reshape(new_shape)
	reshaped_matrix = reshaped_matrix.tolist()
	return reshaped_matrix