print("Hello World")

a = 8
b = 0

try:
    c = a/b
    print(c)
except ConnectionError:
    print("connection error")
except ZeroDivisionError:
    print("error when dividing by zero")

print("done locally at work 2.0")