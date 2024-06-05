import time
import functools
import psutil
import os
        
class timer_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
    
    def __call__(self, *args):
        start_time = time.time()
        val = self.func(*args)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f'Timer {self.func.__name__}: {elapsed_time} seconds')
        return val

class memory_decorator:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
    
    def __call__(self, *args, **kwargs):
        process = psutil.Process(os.getpid())
        mem_before = process.memory_info().rss
    
        val = self.func(*args, **kwargs)

        mem_after = process.memory_info().rss
        memory_used = (mem_after - mem_before) / (1024 * 1024)  # Convert to MB
        print(f'Memory {self.func.__name__}: {memory_used:.4f} MB')
        return val

@memory_decorator
@timer_decorator
def fastest_fibonacci(num):
    result = [0, 1]
    for _ in range(2, num + 1):
        last_value = result[-1]
        new_value = last_value + result[-2]
        result = [last_value, new_value]
    return result[-1]

@memory_decorator
@timer_decorator
def fast_fibonacci(num):
    result = [0, 1]
    for _ in range(2, num + 1):
        result.append(result[-1] + result[-2])
    return result[-1]

print(f'fastest_fibonacci result: {fastest_fibonacci(1000):e}')
print(f'fast_fibonacci result: {fast_fibonacci(1000):e}')