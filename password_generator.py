import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

characters = list(lower_case + upper_case + digits + punctuation)

def generate_password():
    print()
    password_length = int(input('Podaj długość hasła, które chcesz wygenerować: '))
    print()
    random.shuffle(characters)
    password = []

    for i in range(password_length):
        password.append(random.choice(characters))
    
    random.shuffle(password)
    password = ''.join(password)

    print('Wygenerowane hasło: {}'.format(password))
    print()

generate_password()