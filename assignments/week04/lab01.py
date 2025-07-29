def personal_info_manager():
    # Create initial person tuple
    person = ("Boonchoo", 26, "Chonburi", "TH")  # name, age, city, country
    hobbies = []
    
    while True:

        choice = input("What do you want to do? (1: display, 2: add hobby, 3: remove hobby, 4: edit age, 5: exit): ")

        # Your code here
        if choice == "1":
            # display all info
            print("Name: ", person[0])
            print(f"Age: {person[1]}")
            print("City: " + person[2])
            print("Country: ", person[3])
            print("Hobbies: ", hobbies)

        elif choice == "2":
            # append hobby
            hobby = input("What is your new hobbies: ")
            hobbies.append(hobby)

        elif choice == "3":
            # remove hobby
            hobbies.pop()

        elif choice == "4":
            # edit age
            person_list = list(person) # ["Boonchoo", 26, "Chonburi", "TH"]
            age = input("How old are you?: ")
            person_list[1] = age
            person = tuple(person_list)

        elif choice == "5":
            break

if __name__ == "__main__":
    personal_info_manager()