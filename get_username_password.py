from getpass import getpass

def get_username_password():
    username = raw_input('Enter username: ')
    password = getpass('Enter password: ')
    
    return username, password
