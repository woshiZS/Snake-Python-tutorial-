import time

def time_cal(func):
    def wrapper(*args,**kargs):
        start_time = time.time()
        f = func(*args,**kargs)
        exec_time = time.time() - start_time
        print(start_time)
        print(start_time+exec_time)
        return f
    return wrapper

@time_cal
def add(a,b):
    for i in range(10000):
        a+=b
    return a

@time_cal
def sub(a,b):
    return a - b

if __name__ == '__main__':
    add(1,2)