def is_valid_username(username):
    if 4 <= len(username) <= 16 and username.isalnum() and username[0].isalpha() and  username.islower():
        return True
    else:
        return False

print(is_valid_username("alice"))       # True
print(is_valid_username("Alice"))       # False — uppercase
print(is_valid_username("4alice"))      # False — starts with digit
print(is_valid_username("ab"))   