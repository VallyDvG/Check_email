def get_names(nume:str, prenume:str, email:str):
    return nume, prenume, email

def check_email(email:str):
    if email.split("@")[1] == "vodafone.com":
        print("Email is valid")
    else:
        print("Email is not valid")

nume = input("Enter your name: ")
prenume = input("Enter your firstname: ")
email = input("Enter your email: ")

get_names(nume, prenume, email)
check_email(email)
