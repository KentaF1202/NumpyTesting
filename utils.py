import functools
import time

def question(func):
    @functools.wraps(func)
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        duration = time.time() - start
        print("Correct!") if result else print("Incorrect :(")
        print(f"Time elapsed: {duration:.3f} seconds")
        return result
    return wrapper