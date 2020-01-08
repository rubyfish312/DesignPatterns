#%%
def func(num):
    def firstInnerFunc():
        return ("this is the fitst build-in func")

    def secondInnerFunc():
        return ("this is the second build-in func")

    if num == 1:
        return firstInnerFunc
    else:
        return secondInnerFunc
#%%
print(func(1))
print(func(2))
print(func(1)())
print(func(2)())

#%%
firstFunc = func(1)
secondFunc = func(2)
print(firstFunc)
print(secondFunc)
print(firstFunc())
print(secondFunc())

# %%
