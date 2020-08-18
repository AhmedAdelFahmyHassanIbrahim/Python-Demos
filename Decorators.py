def logger(func):
    def wrapper():
        print("Logging an execution")
        func()
        print("Done logging")
    return wrapper

@logger
def sample():
    print("-- inside sample function")

sample()