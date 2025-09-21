password = {"Jim":"123ABC","Tom":"ABCDEFG","Bill":"@BIAJSSK"}
username = input("enter a username:")
if username in password:
    pas = input("enter the password")
    if pas == password[username]:
        print("sucessfully logged in")
    else:
        print("password not found")
else:
    print("username not found")

