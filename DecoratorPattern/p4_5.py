#%%
class TestCall:
    def __init__(self, name):
        self.name = name
 
    def __call__(self, *args, **kwargs):
        print("self.name: %s. " % self.name, end='   ')
        print('__call__()  is  running ')
 
 
if __name__ == '__main__':
    call = TestCall(name='xiaoming')
    call()  # call.__call__(). using this instance as a function
    call.__call__()


# %%
class Fib:
 
    def __call__(self, num, *args, **kwargs):
        n, m, lst = 0, 1, []
 
        for i in range(num):
            lst.append(n)
            n, m = m, n + m
 
        return lst
 
f = Fib()
print(f(10))





# %%
