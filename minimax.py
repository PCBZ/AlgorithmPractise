import numpy as np
import matplotlib.pyplot as plt
import time

def minimax(depth, maximizing_player):
    """
    A simple Minimax implementation for performance testing.
    """
    if depth == 0:
        return np.random.randint(-10, 10)  # Random heuristic value
    
    if maximizing_player:
        best_value = float('-inf')
        for _ in range(6):  # Assume branching factor of 6
            value = minimax(depth - 1, False)
            best_value = max(best_value, value)
        return best_value
    else:
        best_value = float('inf')
        for _ in range(6):
            value = minimax(depth - 1, True)
            best_value = min(best_value, value)
        return best_value

def alpha_beta_pruning(depth, alpha, beta, maximizing_player):
    """
    A simple Alpha-Beta Pruning implementation for performance testing.
    """
    if depth == 0:
        return np.random.randint(-10, 10)  # Random heuristic value
    
    if maximizing_player:
        best_value = float('-inf')
        for _ in range(6):  # Assume branching factor of 6
            value = alpha_beta_pruning(depth - 1, alpha, beta, False)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if beta <= alpha:
                break  # Beta cutoff (pruning)
        return best_value
    else:
        best_value = float('inf')
        for _ in range(6):
            value = alpha_beta_pruning(depth - 1, alpha, beta, True)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if beta <= alpha:
                break  # Alpha cutoff (pruning)
        return best_value

def measure_execution_time(func, depth):
    """
    Measures execution time of the given function.
    """
    start_time = time.time()
    func(depth, True)
    return time.time() - start_time

def plot_complexity():
    """
    Measures and plots execution time complexity for Minimax and Alpha-Beta Pruning.
    """
    depths = np.arange(1, 10, 1)
    minimax_times = [measure_execution_time(minimax, d) for d in depths]
    alpha_beta_times = [measure_execution_time(lambda d, _: alpha_beta_pruning(d, float('-inf'), float('inf'), True), d) for d in depths]
    
    plt.figure(figsize=(8, 5))
    plt.plot(depths, minimax_times, label="Minimax", marker='o', linestyle='--', color='r')
    plt.plot(depths, alpha_beta_times, label="Alpha-Beta Pruning", marker='s', linestyle='-', color='b')
    plt.xlabel("Search Depth (d)")
    plt.ylabel("Execution Time (seconds)")
    plt.yscale("log")  # Log scale to handle exponential growth
    plt.title("Minimax vs Alpha-Beta Pruning Execution Time Complexity")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()

# Run the complexity plot
plot_complexity()
