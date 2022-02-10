import random
import string

lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation

characters = list(lower_case + upper_case + digits + punctuation)

print('')
print('---------- PASSWORD GENERATOR ----------')
print('')

def generate_password():
    option = -1

    while option != '0':
        print('Wybierz opcję: ')
        print('0 - Wyjście z programu')
        print('1 - Generuj nowe hasło')
        print()

        option = input('Wybieram opcję (0 lub 1): ')

        if option == '1':
            print()
            password_length = int(input('Podaj długość hasła, które chcesz wygenerować: '))
            print()

            if password_length < 12:
                print('Twoje hasło powinno składać się minimalnie z 12 znaków!')
                print()
                break
            else:
                print('Generuję hasło...')

            random.shuffle(characters)
            password = []

            for i in range(password_length):
                password.append(random.choice(characters))
    
            random.shuffle(password)
            password = ''.join(password)

            print('Wygenerowane hasło: {}'.format(password))
            print()
        elif option == '0':
            print()
            print('---------- DO ZOBACZENIA! ----------')
            print()

generate_password()