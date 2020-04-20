import time
from functools import wraps
def timer(name):

    def _timer(func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            stop = time.perf_counter()
            print(f'Runtime of <{name}>: {stop - start:0.4f} seconds')
            return result

        return wrapper

    return _timer
        
