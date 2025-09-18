import timeit, tracemalloc
import numpy as np
from sklearn.metrics import r2_score

def measure_time(func, sizes):
    results = []
    for n in sizes:
        t = timeit.timeit(lambda: func(n), number=3)
        results.append((n, t))
    return results

def estimate_complexity(data):
    n_vals, t_vals = zip(*data)
    candidates = {
        "O(1)": lambda n: np.ones_like(n),
        "O(log n)": lambda n: np.log2(n),
        "O(n)": lambda n: n,
        "O(n log n)": lambda n: n*np.log2(n),
        "O(n^2)": lambda n: n**2,
    }
    scores = {}
    n_arr, t_arr = np.array(n_vals), np.array(t_vals)
    for name, f in candidates.items():
        pred = f(n_arr)
        pred = pred / pred[-1] * t_arr[-1]  # normalize scale
        scores[name] = r2_score(t_arr, pred)
    return max(scores, key=scores.get)

# Example
def test_func(n): return [i**2 for i in range(n)]

sizes = [100, 200, 400, 800, 1600]
data = measure_time(test_func, sizes)
print(data)
print("Estimated complexity:", estimate_complexity(data))
