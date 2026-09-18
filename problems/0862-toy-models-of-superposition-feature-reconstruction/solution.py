import numpy as np

def superposition_reconstruct(W, b, X):
    """
    Compute reconstructed features for the toy superposition model.

    Args:
        W: array of shape (n_hidden, n_features)
        b: array of shape (n_features,)
        X: array of shape (batch_size, n_features)

    Returns:
        list of lists of shape (batch_size, n_features) with reconstructed features
    """
    T = []

    W = np.array(W)
    X = np.array(X)
    b = np.array(b)

    for x in X:
        hidden = W @ x
        decoded = W.T @ hidden
        decoded += b
        decoded = np.maximum(0, decoded)
        T.append(decoded)
    return T
