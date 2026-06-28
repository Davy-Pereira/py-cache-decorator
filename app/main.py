from typing import Any, Callable


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args: Any) -> Any:
        if args in data:
            print("Getting from cache")
            return data[args]

        print("Calculating new result")
        result = func(*args)
        data[args] = result
        return result