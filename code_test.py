def a(x, y):
    print("a")
    return 1

def b(z):
    print("b")
    return 2

print(a(b(a(1, 1)) + b(3), 1))