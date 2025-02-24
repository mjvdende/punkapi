from functools import wraps

def curry(func):
    @wraps(func)
    def curried(*args):
        if len(args) < func.__code__.co_argcount:
            return lambda *more_args: curried(*(args + more_args))

        return func(*args)

    return curried
