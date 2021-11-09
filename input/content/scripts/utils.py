from browser import timer

def repeat(seconds, start=False):
    def decorator(f):
        def wrapper(*args, **kwargs):
            timer.set_timeout(wrapper, seconds * 1000)
            return f(*args, **kwargs)
        if start:
            wrapper()
        return wrapper
    return decorator
