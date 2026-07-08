# Decorator-1
def add_sprinkel(func):
    def wrapper(*args, **kwargs):
        print(f"You add {kwargs['Quantity'][1]} sprinkel")
        func(*args, **kwargs)
    return wrapper

# Decorator-2
def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("You add fudge")
        func(*args, **kwargs)
    return wrapper

@add_sprinkel
@add_fudge
def get_icecream(flavor, **Quantity):
    print(f"Here is your {flavor} icecream")

get_icecream("chocolate", Quantity=["Light", "Medium", "Heavy"])

"""
NB: 
1# Without the wrapper function inside the definition of decorator, it will be invoked as soon as it's being used as decorator on top of any function.
2# Multiple decorators can be used on top of the same function.

Task:
1. Write more examples of python decorators.
"""