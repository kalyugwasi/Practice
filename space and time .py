import timeit
import tracemalloc

def test_function(n):
    return [i**2 for i in range(n)]

# Time measurement
execution_time = timeit.timeit(lambda: test_function(10_000), number=10)
print(f"Execution time: {execution_time:.6f} seconds")

# Memory measurement
tracemalloc.start()
test_function(10_000)
current, peak = tracemalloc.get_traced_memory()
print(f"Current memory: {current/1024:.2f} KB; Peak memory: {peak/1024:.2f} KB")
tracemalloc.stop()
