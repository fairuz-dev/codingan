def validasi_email(email):
    if "@" in email and email.endswith(".com"):
        return True
    else:
        return False

email = "fairuzcutee@gmail.com"
hasil = validasi_email(email)
print("Email valid:", hasil)
