def rejection_sampling_best_of_k(candidates, scores):
    """
    Select the highest-scoring candidate per prompt.

    Args:
        candidates: list of N lists, each containing K candidate outputs.
        scores: list of N lists, each containing K reward scores.

    Returns:
        List of N selected candidates.
    """

    P = []

    for i in range(len(candidates)):
        T = max(scores[i])

        Tr = scores[i].index(T)

        P.append(candidates[i][Tr])

    return P