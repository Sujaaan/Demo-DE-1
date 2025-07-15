def logtime(func):
    def wrapper(*args,**kwargs):
        print("I am from logtim => wrapper")
        result = func(*args,**kwargs)
        print("function ended")
        return result
    return wrapper

@logtime
def process():
    print("I am printing from the process method")

process()