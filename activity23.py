#Jeepney Simulator
passenger_name = []
passengers = ["Ana", "Ben", "Carla"]
print(passengers)
passengers.append("Dan")
print(passengers)
passengers.insert(0, "Lola")
print(passengers)
passengers.remove("Ben")
x = passengers.pop()
y = passengers.pop(0)
len(passengers)
"Ana" in passengers == True
passengers.reverse()

#Jeepney Simulator Iteractive
route = ["Terminal", "Perez Park", "Pacific Mall"]
passengers = []
SEATS = 6
FARE = 13
total = 0

while True:
    print()
    print("Sakay:", passengers)
    print(len(passengers), "of", SEATS, "seats")
    print("1 sakay  2 Priority seat 3 para po!")
    print("4 Baba sa pinto  5 Baba sa harap")
    print("6 seat check 7 balikan   8 Exit")
    choice = input("Choice: ")

    if choice == "1":
        if len(passengers) == SEATS:
            print("puno na!")
        else:
            name = input("Name: ")
            passengers.append(name)
            total = total + FARE
            print(name, "Boarded at the back")

    elif choice == "2":
        if len(passengers) == SEATS:
            print("puno na!")
        else:
            name = input("Name: ")
            passengers.insert(0, name)
            total = total + FARE
            print(name, "took the priority seat")

    elif choice == "3":
        name = input("Who is getting off?   ")
        if name in passengers:
            passengers.remove(name)
            print(name, "got off. ingat!")
        else:
            print(name, "is not on this jeep")

    elif choice == "4":
       if len(passengers) == 0:
           print(left, "got off at the door")

    elif choice == "5":
        if len(passengers) == 0:
            print("The jeep is empty")
        else:
            front = passengers.pop(0)
            print(front, "got off at the front")

    elif choice == "6":
        for i in range(len(passengers)):
            print("Seat", i + 1, passengers[i])

    elif choice == "7":
        route.reverse()
        print("Route:", route)

    elif choice =="8":
        print("Total fare today:", total)
        break

    