import time


def timer(f):
    def wrapper(*args):
        start_time = time.time()
        result = f(*args)
        end_time = time.time()
        print('%r took: %2.3f sec' % (f.__name__, end_time - start_time))
        return result
    return wrapper
