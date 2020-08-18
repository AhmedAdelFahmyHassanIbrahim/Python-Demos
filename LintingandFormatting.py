x = 42

def demo():
    return 'Wibble'
    print("Hello")

def print_hello(name: str) -> str:
    """
    Returns a greeting

    parameters:
        name (str): the name of the person
    
    Returns:
        The cools message
    """
    print('Hello, ' + name)

print_hello()