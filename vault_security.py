def check_password(pwd):
    # mínim 8 caràcters
    if len(pwd) < 8:
        return False

    # ha de tenir almenys un número
    if not any(char.isdigit() for char in pwd):
        return False

    # ha de tenir almenys una majúscula
    if not any(char.isupper() for char in pwd):
        return False

    # no pot contenir la paraula "admin" (case insensitive)
    if "admin" in pwd.lower():
        return False

    return True
