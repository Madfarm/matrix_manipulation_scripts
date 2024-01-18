import time
from functools import wraps

def measure_time(func):
    """Decorator to measure function execution time in milliseconds."""

    @wraps(func)  # Preserve function metadata
    def wrapper(*args, **kwargs):
        start_time = time.time() * 1000   # Time in milliseconds
        result = func(*args, **kwargs)
        end_time = time.time() * 1000
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' took {execution_time:.2f} ms to execute.")
        return result
    return wrapper

@measure_time
def my_function():
    # Do some time-consuming operations here
    time.sleep(1)  # Simulate a 1-second delay

if __name__ == "__main__":
    my_function()