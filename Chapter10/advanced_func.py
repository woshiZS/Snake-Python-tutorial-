def square(x):
    '''Square of x'''
    return x*x

def cube(x):
    '''Return cube of x'''
    return x*x*x

funcs = {
    'sqa':square,
    'cb':cube,
}

# x = 2

# print(square(x))
# print(cube(x))

# for func in sorted(funcs):
#     # 这里的func输出的是key的值
#     print(func,funcs[func](x))

def mod(x):
    x = [997,998,999]
    return x

x = [1,2,3]

# print(x)
# print(mod(x))
# print(x)

def f(x = None):
    if x is None:
        x = []
    x.append(1)
    return x

print(f())
print(f())
print(f())
print(f(x = [9,9,9]))
print(f())
print(f())
