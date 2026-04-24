def checkEmail(email):
    if email.count('@') != 1:
        return False

    local, domain = email.split('@')

    if not local or not domain:
        return False

    if '.' not in domain:
        return False

    if domain.startswith('.') or domain.endswith('.'):
        return False

    parts = domain.split('.')
    if any(part == '' for part in parts):
        return False

    if len(parts[-1]) < 2:
        return False

    return True


email = input("Moi nhap dia chi email: ")

if checkEmail(email):
    print("Email hop le")
else:
    print("Email khong hop le")

