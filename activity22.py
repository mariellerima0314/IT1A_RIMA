anime_type = ["isekai", "adventure", "scifi", "manhwa"]
anime_title = []

while True:
    ans = input("Are you familiar with anime? ---> (yes/no)")

    if ans.lower() == 'yes':
        print("What type? Select from the list:")
        for x in anime_type:
            print(x) #traversing a list

            a_type = input("Type -->    ")

            title = input("What is the title of the anime?  ")
            anime_title.append(title)
            continue
        else:
            print("Thank You")
            break