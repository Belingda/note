#coding=utf-8
import sys
class NEWFUNC(object):
    def __init__(self,func):
        self.func=func
    def __call__(self,*args):
        print("replace function args%s"%str(args))
        self.func(*args)
        
def test1(a,b):
    print("enter test1() a=%d,b=%d"%(a,b))

def printdebug(funcname):
    '''
    指定函数名
    重写函数(call方法 关键 )
    在模块找到函数并替换
    '''
    funcd=sys.modules['__main__'].__dict__
    for name,func in funcd.items():
        if name==funcname:
            newfunc=NEWFUNC(func)
            funcd[funcname]=newfunc
            break

printdebug('test1')            
test1(1,2)
