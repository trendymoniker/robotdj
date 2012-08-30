from getpass import getpass

def get_password(prompt='Enter password: '):
    return getpass(prompt)

def get_username(prompt='Enter username: '):
    return raw_input(prompt)

def get_username_password(prompt=None):
    if prompt:
        print prompt

    username = get_username()
    password = get_password()
    
    return username, password
