from builtins import print
import functools

def decorator (func):
    @functools.wraps(func)
    def wrapped(text):
        wrapped.num_calls += 1
        if len(text) > 10 and wrapped.num_calls <= 5:
            func(text)
        else:
            pass

    wrapped.num_calls = 0
    return wrapped


print = decorator(print)

print("small")
print("more than 5")
print("3rd time called")
print("4th time print called")
print("5th time print called - Should be the last print")
print("6th time print called - should not print")



