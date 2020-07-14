file_name='test.txt'
with open(file_name) as f:
    c_st = f.read()
    print(len(c_st))