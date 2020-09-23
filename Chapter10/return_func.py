def make_logger(target):
    def logger(data):
        with open(target,'a') as f:
            f.write(data + '\n')
    return logger

foo_logger = make_logger('foo.txt')
foo_logger('Hello')
foo_logger('World')