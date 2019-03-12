#!/usr/bin/python3
import inspect
import sys

def tracefunc(frame, event, arg):
    if event == 'return':
        print('function:', frame.f_code.co_name, ', local vars',
              [k for k, v in inspect.currentframe().f_back.f_locals.items()])
    return tracefunc


def foo():
    friends = ['A', 'B']
    for f in friends:
        print('Hi ' + f)
    return len(friends)

def tracefoo(to_trace):
    sys.settrace(tracefunc)
    return to_trace(), sys.settrace(None)




if __name__ == '__main__':
   tracefoo(foo)



