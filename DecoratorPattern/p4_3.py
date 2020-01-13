#%%
import logging
logging.basicConfig(level=logging.INFO)
#%%
def loggingDecorator(func):
    """decorator of write log"""
    """function decorator"""
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
# " print the fuction name and its args "

# showInfo()
# this is a testing func :  () {}
# " () means actually calling but there is no args "

# showInfo('arg1','arg2',kwarg1 = 1, kwarg2 = 2)
# this is a testing func :  ('arg1', 'arg2') {'kwarg1': 1, 'kwarg2': 2}
# " put some real args :  'arg1','arg2',kwarg1 = 1, kwarg2 = 2 into function "

#%%
# loggingDecorator
# <function __main__.loggingDecorator(func)>
# " print the fuction name and its args,  
#   in this case we must put a required arg "

# loggingDecorator(showInfo)
# <function __main__.loggingDecorator.<locals>.wrapperLogging(*args, **kwargs)>
# " run the function which is in the loggingDecorator "

# loggingDecorator(showInfo())
# this is a testing func :  () {}
# <function __main__.loggingDecorator.<locals>.wrapperLogging(*args, **kwargs)>
# " showInfo() means calling  the function of function of function until the showInfo
#   function, but in this case, there is no arg in showInfo() " 

# loggingDecorator(showInfo)('arg1','arg2',kwarg1 = 1,kwarg = 2)
# INFO:root: start showInfo() ...
# this is a testing func with args :  ('arg1', 'arg2') {'kwarg1': 1, 'kwarg': 2}
# INFO:root: showInfo() finish
# " run into the rightest ('arg1','arg2',kwarg1 = 1,kwarg = 2)"

#loggingDecorator(showInfo('arg1','arg2',kwarg1 = 1,kwarg = 2))
# this is a testing func with args :  ('arg1', 'arg2') {'kwarg1': 1, 'kwarg': 2}
# <function __main__.loggingDecorator.<locals>.wrapperLogging(*args, **kwargs)>
# " only print showInfo('arg1','arg2',kwarg1 = 1,kwarg = 2) "

#%%
#decoratedShowInfo = loggingDecorator(showInfo)
#decoratedShowInfo('arg1','arg2',kwarg1 = 1,kwarg = 2)
# INFO:root: start showInfo() ...
# this is a testing func with args :  ('arg1', 'arg2') {'kwarg1': 1, 'kwarg': 2}
# INFO:root: showInfo() finish


#%%
def showMin_1(a, b):
     print("%d, %d and the sum is %d" % (a,b,a+b))


#%%
decoratedShowMin = loggingDecorator(showMin_1)
decoratedShowMin(2, 3)    

# %%
@loggingDecorator
def showMin_2(a, b):
     print("%d, %d and the sum is %d" % (a,b,a+b))

# %%
showMin_2(2, 3)

# %%
