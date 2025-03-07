
# Menu untuk register user dengan validasi nama, email, dan password
full_name = ""
email = ""
password = ""

while True:
    print("""Signup to App
1. Full Name
2. Email
3. Password
4. Submit""")
    option = int(input("Pick an option >> "))
    while option < 1 or option > 4:
        option = int(input("Pick an option (1, 2, 3, 4) >> "))

    # Input Full Name
    if option == 1:
        full_name = input("Enter your full name: ")
        # Validasi nama harus capital letter
        while not full_name.istitle():
            print("Name must start with capital letter! Try again")
            full_name = input("Enter your full name: ")
        print("Success! \n")

    # Input Email
    elif option == 2:
        email = input("Enter your email: ")
        # Validasi email harus ends with @gmail.com
        while not email.endswith("@gmail.com"):
            print("Invalid input! Email must end with '@gmail.com'")
            email = input("Enter your email: ")
        print("Success! \n")

    # Input Password
    elif option == 3:
        password = input("Enter your password: ")
        # Validasi password panjangnya harus atleast 8 karakter
        while len(password) < 8:
            print("Invalid input! Password must be atleast 8 characters!")
            password = input("Enter your password: ")
        print("Success! \n")
    
    # Check if Email and Password is input
    elif option == 4:
         # Validasi harus ada semua untuk submit
         if full_name and email and password:
            print("User registered succesfully")
            break
         else:
            print("Please fill in all inputs! \n")