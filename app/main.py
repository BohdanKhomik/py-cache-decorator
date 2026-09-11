from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args, **kwargs) -> Callable:

        if func in cache:
            if args + tuple(kwargs.items()) in cache[func]:
                print("Getting from cache")
                return cache[func][args]
            else:
                print("Calculating new result")
                result = func(*args, **kwargs)
                cache[func][args + tuple(kwargs.items())] = result
                return result
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[func] = {args + tuple(kwargs.items()) : result}
            return result

    return wrapper
