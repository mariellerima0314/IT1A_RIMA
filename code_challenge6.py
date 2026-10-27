size = (int(input("Enter size: ")))
current_number = 1
for x in range(1, size + 1):
    for y in range(x):
        print(current_number, end=" ")
        current_number += 1
    print()