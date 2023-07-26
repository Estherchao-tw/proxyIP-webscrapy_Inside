import timeit

# python -m timeit "'-'.join(str(n) for n in range(100))" 

# start = time.time()
def f():
    import os
    for path,dirs,files in os.walk('.'):
        print(path)
        for f in files:
            print(os.path.join(path,f))

        for d in dirs:
            print(os.path.join(path,d))
    # time.sleep(1)
    # end = time.time()


# print('total time : {}'.format(end-start))
print(timeit.timeit(f,number=5))
