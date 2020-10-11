def outer(func):
    def inner():
        print('*********************')
        func()
        print('*********************')
    return inner

@outer
def myFunc():
    print('sunck is a good man.')

myFunc()