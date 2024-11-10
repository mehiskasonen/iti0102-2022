a = {"Bernard": 100, "Adolf": 1000, "Donald": 999, "Charlie": 10}
b = {i: a[i] for i in reversed(list(a.keys()))}
c = {i: a[i] for i in sorted(list(a.keys()))}
d = {i: a[i] for i in sorted(list(a.keys()), reverse=True)}
e = {i: a[i] for i in sorted(a.keys(), key=len)}
f = {i: a[i] for i in sorted(a.keys(), key=len, reverse=True)}
print("a: " + str(a))
print("b: " + str(b))
print("c: " + str(c))
print("d: " + str(d))
print("e: " + str(e))
