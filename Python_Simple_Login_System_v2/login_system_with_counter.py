import hashlib
import csv

def signup():
    email = input("Enter email address: ")
    pwd = input("Enter password: ")
    conf_pwd = input("Confirm password: ")

    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("credentials.csv", mode="w") as f:
            credential_writer = csv.writer(f, delimiter=',', quotechar='"')
            credential_writer.writerow([email, hash1])
        f.close()
        print("You have registered successfully!")
    else:
        print("Password is not the same as above! \n")

def login():
    counter = 0
    counter_limit = 2
    out_of_limits = False
    email = input("Enter email: ")
    pwd = input("Enter password: ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("credentials.csv", "r") as f:
        stored_email, stored_pwd = f.read().split()
    f.close()
    if email != stored_email or auth_hash != stored_pwd and out_of_limits:
        print("Wrong credentials! Please try again.")
        print("Login attempts left: " + str(counter_limit))
    while email != stored_email or auth_hash != stored_pwd:
        if counter < counter_limit:
            email = input("Enter email: ")
            pwd = input("Enter password: ")
            auth = pwd.encode()
            auth_hash = hashlib.md5(auth).hexdigest()
            counter += 1
            if counter <= 1:
                print("Wrong credentials! Please try again.")
                print("Login attempts left: " + str(counter))
        else:
            out_of_limits = True
            break

    if out_of_limits:
         print("Login failed!")
    else:
         print("Logged-in successfully!")

while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong Choice!")