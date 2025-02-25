while True:
    ch = input(
        "Name: vivek kumar SAT-1\n"
        "A program that converts temperatures from Fahrenheit to Celsius and vice versa.\n"
        "1. Find Celsius\n"
        "2. Find Fahrenheit\n"
        "3. Exit\n"
        "Please enter your choice: "
    )

    if ch == '1':
        f = float(input("Enter your Fahrenheit value: "))
        print("Celsius =", (5 / 9) * (f - 32))

    elif ch == '2':
        c = float(input("Enter your Celsius value: "))
        print("Fahrenheit =", (9 / 5) * c + 32)

    elif ch == '3':
        print("Thank you!")
        break

    else:
        print("Please enter a valid choice...\n")