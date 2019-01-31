def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

@decorator
def return_greeting(name):
    print("Creating greeting")
    return "Hi " + name

@decorator
def return_greeting(name, age):
    print("Creating greeting")
    return "Hi " + name + ' you are ' + age + ' years old.'

a = return_greeting('Trishant')
print(a)

a = return_greeting('Trishant Pahwa', "22")
print(a)