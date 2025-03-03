import time

def Cache(func):
    cache_value = {}
    def wrapper(*args,**kwargs):
        if args in cache_value:
            return cache_value[args]
        result = func(*args,**kwargs)
        cache_value[args] = result
        return result
    return wrapper

@Cache
def long_run_time(a,b):
    time.sleep(4)
    return a+b

print(long_run_time(2,3))
print(long_run_time(2,3))
