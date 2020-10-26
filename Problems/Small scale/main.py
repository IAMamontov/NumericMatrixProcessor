s = input()
a = []
while s != ".":
    a.append(float(s))
    s = input()

print(min(a))