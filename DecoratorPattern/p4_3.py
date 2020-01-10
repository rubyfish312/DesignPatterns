#%%
import logging
logging.basicConfig(level=logging.INFO)
#%%
def loggingDecorator(func):
    """decorator of write log"""
    def wrapperLogging(*args, **kwargs):
        logging.info(" start %s() ..." % func.__name__)
        func(*args, **kwargs)
        logging.info(" %s() finish" % func.__name__)
    return wrapperLogging

#%%
def showInfo(*args, **kwargs):
    print("this is a testing func with args : ", args, kwargs)

#%%
# showInfo
# <function __main__.showInfo(*args, **kwargs)>

# showInfo()
# this is a testing func :  () {}

# showInfo('arg1','arg2',kwarg1 = 1, kwarg2 = 2)
# this is a testing func :  ('arg1', 'arg2') {'kwarg1': 1, 'kwarg2': 2}

#%%
# loggingDecorator(showInfo)
# <function __main__.loggingDecorator.<locals>.wrapperLogging(*args, **kwargs)>

# loggingDecorator(showInfo())
# this is a testing func :  () {}
# <function __main__.loggingDecorator.<locals>.wrapperLogging(*args, **kwargs)>

# loggingDecorator(showInfo)('arg1','arg2',kwarg1 = 1,kwarg = 2)
# INFO:root: start showInfo() ...
# this is a testing func with args :  () {}
# INFO:root: showInfo() finish

# loggingDecorator(showInfo())()
# decoratedShowInfo = loggingDecorator(showInfo)
# AttributeError: 'NoneType' object has no attribute '__name__'

#%%
#decoratedShowInfo = loggingDecorator(showInfo)
#decoratedShowInfo('arg1','arg2',kwarg1 = 1,kwarg = 2)
# INFO:root: start showInfo() ...
# this is a testing func with args :  ('arg1', 'arg2') {'kwarg1': 1, 'kwarg': 2}
# INFO:root: showInfo() finish

# %%
# def showMin(a, b):
#     print("%d, %d the min in %d" % (a,b,a+b))

# decoratedShowMin = loggingDecorator(showMin)
# decoratedShowMin(2, 3)


# %%
# @loggingDecorator
# def showMin(a, b):
#     print("%d, %d the min in %d" % (a,b,a+b))

#showMin(2, 3)    

# %%
