from typing import Any, Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any) -> Any:
        if args in storage:
            print("Gatting from cache")
            return storage[args]
        print("Calculating new result")
        result = func(*args)
        storage[args] = result
        return result
    return wrapper
