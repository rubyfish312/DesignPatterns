#%%
import logging

#%%
logging.basicConfig(level=logging.INFO)

def loggingDecorator(func):
    """decorator of write log"""
    def wrapperLogging(*args, **kwargs):
        logging.info("start %s() ..." % func.__name__)
        func(*args, **kwargs)
        logging.info("%s() finish" % func.__name__)
    return wrapperLogging

def showInfo(*args, **kwargs):
    print(" this is a testing func : ", args, kwargs)

decoratedShow = loggingDecorator(showInfo)
decoratedShow('arg1','arg2',kwarg1 = 1, kwarg2 = 2)

# %%
# def showMin(a, b):
#     print("%d, %d the min in %d" % (a,b,a+b))

# decoratedShowMin = loggingDecorator(showMin)
# decoratedShowMin(2, 3)


# %%
@loggingDecorator
def showMin(a, b):
    print("%d, %d the min in %d" % (a,b,a+b))

showMin(2, 3)    

# %%
