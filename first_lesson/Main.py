import time
from functools import wraps


def timing_decorator(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # זמן התחלה
        result = func(*args, **kwargs)  # קריאה לפונקציה
        end_time = time.time()  # זמן סיום
        execution_time = end_time - start_time
        print(f"Function {func.__name__} took {execution_time:.6f} seconds to run")
        return result
    return wrapper


def cache_decorator(func):
    cache = {}
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Using cached result for {func.__name__}{args}")
            return cache[args]
        result = func(*args)
        cache[args] = result  # שמירת התוצאה בזיכרון
        return result
    return wrapper


@timing_decorator
def fibonacci_no_cache(n):
    if n <= 1:
        return n
    return fibonacci_no_cache(n - 1) + fibonacci_no_cache(n - 2)


@timing_decorator
@cache_decorator
def fibonacci_with_cache(n):
    if n <= 1:
        return n
    return fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)


print("Without Cache:")
fibonacci_no_cache(30)  # ייקח הרבה זמן

print("\nWith Cache:")
fibonacci_with_cache(30)  # יהיה מהיר יותר
