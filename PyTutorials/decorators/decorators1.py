import random
PLUGINS = []

def register(func):
    """Register a function as a plug-in"""
    # PLUGINS[func.__name__] = func
    # return func
    func = (func.__name__, func)
    PLUGINS.append(func)

@register
def say_hello(name):
    return "Hello " + name

@register
def be_awesome(name):
    return "Yo " + name + ", together we are the awesomest!"

def randomly_greet(name):
    print(PLUGINS)
    greeter = PLUGINS[0][1]
    return greeter(name)

greeting = randomly_greet('Trishant Pahwa')
print(greeting)