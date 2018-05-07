import timeit
from functools import wraps


def profile(param):
    if isinstance(param, type):
        for attr_name in param.__dict__:
            if callable(getattr(param, attr_name)):
                print(attr_name)
                method = profile(getattr(param, attr_name))
                setattr(param, attr_name, method)
        return param
    else:
        @wraps(param)
        def timer(*args):
            print(param.__name__, "Started")
            a = timeit.default_timer()
            x = param(*args)
            print(param.__name__ + " finished in " + str(timeit.default_timer() - a) + " s")
            #print(timeit.timeit("func(data)", setup="from __main__ import func, data", number=2))
            return x
        return timer


@profile
def counter(*args):
    return sum(args)


@profile
class Example:
    def __init__(self, attr):
        self.attr = attr

    def get(self):
        return self.attr

    def set(self, attr):
        self.attr = attr

    def clear(self):
        del self.attr


counter(6, 8, 9, 10,10,10,10,10,10,1,1,1,1,1,1,1,3,5,6,8,7,5,4,2,2,4,6,7,8,8,6,5,43,2,2,2,34,5,6,7,7,8,8,9)


counter(1, 4, 5, 6, 7, 8, 10, 96)


A = Example(1)
A.get()
A.set(1)


#print(timeit.timeit("counter()", setup="from __main__ import counter", number=1))

