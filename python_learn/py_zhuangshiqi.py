'''装饰器'''
def log(func):
    def wrapper(*args, **kw):
        print('log:--------- call %s():' % func.__name__ ,"--------------")
        return func(*args, **kw)
    return wrapper

# @log
# def add(x,y):
#     return x+y
# print(add(1,2))

@log
def console():
    return print("test")
console()