def differential_sarsa(transitions: dict, initial_state: str, alpha: float, beta: float, num_steps: int) -> tuple:
    """
    Differential Sarsa for the average-reward continuing setting.
    
    Args:
        transitions: dict mapping (state, action) -> (reward, next_state)
        initial_state: starting state
        alpha: step size for Q-value updates
        beta: step size for average reward estimate
        num_steps: number of steps to simulate
    
    Returns:
        Tuple of (Q, R_bar) where Q is a dict {(state, action): float}
        and R_bar is a float.
    """
    Q = {}

    for state_action in transitions:
        Q[state_action] = 0.0

    R_bar = 0.0
    state = initial_state

    for _ in range(num_steps):
        actions = [a for (s, a) in Q if s == state]
        action = min(actions, key=lambda a: (-Q[(state, a)], a))

        reward, next_state = transitions[(state, action)]

        next_actions = [a for (s, a) in Q if s == next_state]
        next_action = min(next_actions, key=lambda a: (-Q[(next_state, a)], a))

        delta = (
            reward
            - R_bar
            + Q[(next_state, next_action)]
            - Q[(state, action)]
        )

        R_bar += beta * delta
        Q[(state, action)] += alpha * delta

        state = next_state

    return Q, R_bar