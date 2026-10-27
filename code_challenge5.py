for a in range(5):
    for b in range(5):
        if a + b == 5-1 or a == b:
            print(b, end=" ")
        else:
            print(" ", end="")
    print()
print("----------")
for c in range(5):
    for d in range(5):
        if c + d == 5-1 or c == d:
            print("*", end=" ")
        else:
            print(" ", end="")
    print()
print("----------")
n = int(input("Input size of x "))
for x in range(n):
    for y in range(n):
        if x + y == n-1 or x == y:
            print("*", end=" ")
        else:
            print(" ", end="")
    print()