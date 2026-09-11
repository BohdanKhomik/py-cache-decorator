from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:

        if func.__name__ in cache.keys():
            if args in cache[func.__name__]:
                print("Getting from cache")
                return cache[func.__name__][args]
            else:
                print("Calculating new result")
                result = func(*args, **kwargs)
                cache[func.__name__][args] = result
                return result
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[func.__name__] = {args : result}
            return result

    return wrapper
