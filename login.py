import csv


def main():
    user = input("Register or Login:(r or l): ")
    with open("LoginInformation.txt", "r") as file:
        file_reader = csv.reader(file)
        if user == "r":
            register(file_reader)
            file.close()

        else:
            username_check(file_reader)
            file.close()


def username_check(file):
    user = input("Type your username: ")
    for row in file:
        if row[0] == user:
            print("found")
            password = input("Type your password: ")
            if row[1] == password:
                print("Login successful")
            else:
                print("Wrong password! ")


def register(file1):
    user = input("Username: ")
    file = open("LoginInformation.txt", "a")
    exist = False
    for row in file1:
        if row[0] == user:
            print("already exist")
            exist = True
    if not exist:
        file.write('\n'+user)
        file.write(",")
        password = input("Password: ")
        file.write(password)
    file.close()


main()
