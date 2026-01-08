import numpy as np
from scipy.stats import binom
from scipy.special import comb
import matplotlib.pyplot as plt
from tqdm import tqdm

def binomial_tail(n, k_min, p):
    """Calculate P(X >= k_min) for X ~ Binomial(n, p)"""
    if p == 0:
        return 1.0 if k_min == 0 else 0.0
    if p == 1:
        return 1.0 if k_min <= n else 0.0
    if k_min > n:
        return 0.0
    return binom.sf(k_min-1, n, p)

def check_conditions(x, y, p1, p2, x0, y0, threshold=0.9):
    if not isinstance(x, int) or not (isinstance(y, int)) or x <= 0 or y <= 0:
        raise ValueError("x and y must be positive integers")
    if not 0 <= x0 <= x or not 0 <= y0 <= y:
        raise ValueError("x0 and y0 must be within bounds")
    if not 0 < p1 < 1 or not 0 < p2 < 1:
        raise ValueError("p1 and p2 must be between 0 and 1")

    prob1 = min(max(p1**y, 0), 1)  # Clamp probability
    sum1 = binomial_tail(x, x0, prob1)
    
    prob2 = min(max(p2**x, 0), 1)  # Clamp probability
    sum2 = binomial_tail(y, y0, prob2)
    
    return sum1 >= threshold, sum2 >= threshold, sum1, sum2

def find_solutions(p1, p2, x0, y0, x_max=50, y_max=50):
    solutions = []
    for x in tqdm(range(x0, x_max)):
        for y in range(y0, y_max):
            cond1, cond2, sum1, sum2 = check_conditions(x, y, p1, p2, x0, y0)
            if cond1 and cond2:
                solutions.append((x, y, sum1, sum2))
                # print(f"Solution: x={x}, y={y}")
                # print(f"  P1: {sum1:.4f}, P2: {sum2:.4f}")
                # print("-" * 30)
    return solutions

def plot_results(solutions, all_points, p1, p2, x0, y0):
    plt.figure(figsize=(10, 10))
    
    x_sol = [x for x, y, is_sol, *_ in all_points if is_sol]
    y_sol = [y for x, y, is_sol, *_ in all_points if is_sol]
    x_non = [x for x, y, is_sol, *_ in all_points if not is_sol]
    y_non = [y for x, y, is_sol, *_ in all_points if not is_sol]
    
    plt.scatter(x_non, y_non, color='red', label='Not safe', alpha=0.5)
    plt.scatter(x_sol, y_sol, color='green', label='Safe', s=100, edgecolor='black')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'p1={p1}, p2={p2}, x0={x0}, y0={y0}')
    plt.legend()
    plt.grid(True)
    plt.show()

# Parameters
p1_val, p2_val = 0.99, 0.90
x0_val, y0_val = 5, 5
x_max = y_max = 100

# Find solutions
print(f"Parameters: p1={p1_val}, p2={p2_val}, x0={x0_val}, y0={y0_val}\n")
solutions = find_solutions(p1_val, p2_val, x0_val, y0_val, x_max, y_max)

if not solutions:
    print("No solutions found in the given ranges.")
else:
    print(f"\nFound {len(solutions)} solution(s).")

# Generate all points for plotting
all_points = []
for x in tqdm(range(x0_val, x_max)):
    for y in range(y0_val, y_max):
        cond1, cond2, sum1, sum2 = check_conditions(x, y, p1_val, p2_val, x0_val, y0_val)
        all_points.append((x, y, cond1 and cond2, sum1, sum2))

plot_results(solutions, all_points, p1_val, p2_val, x0_val, y0_val)