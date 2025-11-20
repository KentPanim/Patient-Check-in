print("'Please log in to use the system'")
print("")

email_1 = "medicalteam"
passwrd = "12345"

login1 = input("Enter email: ")
login2 = input("Enter password: ")

while login1 != email_1 or login2 != passwrd:
    print("Invalid email or password, please try again")
    login1 = input("Enter email: ")
    login2 = input("Enter password: ")

print("You are logged in!\n")

patients = []
current_index = 0
queue_num = 1

while True:
    print("Type '1' to view list of patients")
    print("Type '2' to register patient and concern")
    print("Type '3' to exit")

    option_in = int(input("Enter option: "))

    if option_in == 1:
        print("\nHere are the list of patients:")
        if len(patients) == 0:
            print("No patients registered yet.\n")
        else:
            for i, p in enumerate(patients, start=1):
                print(f"{i}. Name: {p['name']} | Concern: {p['concern']}")
            print()

            while True:
                ask = input("Type 'next' to call the next patient or press Enter to go back: ")

                if ask.lower() == "next":
                    if current_index < len(patients):
                        print(f"Calling patient: {patients[current_index]['name']}\n")
                        current_index += 1
                    else:
                        print("No more patients in queue.\n")
                    break

                elif ask == "":
                    break

                else:
                    print("Invalid input. Please type 'next' or press Enter.\n")

    elif option_in == 2:
        print("\nEnter 'x' anytime to stop registering.")

        while True:
            name = input("Enter patient name (type 'x' to stop): ")
            if name.lower() == "x":
                break

            concern = input("Enter concern (type 'x' to stop): ")
            if concern.lower() == "x":
                break

            patients.append({"name": name, "concern": concern})
            print("Patient registered successfully! Queue number:", queue_num)
            queue_num += 1

    elif option_in == 3:
        print("Exiting system...")
        break

    else:
        print("Invalid option. Try again.\n")
