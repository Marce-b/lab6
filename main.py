#Marcel Bossa
def print_menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()


def decode(password):
    decoded = ""
    for digit in password:
        decoded += str((int(digit)-3)%10)
    return decoded


def encode(password):
    encoded = ""
    for digit in password:
        new_digit = (int(digit) + 3) % 10
        encoded += str(new_digit)
    return encoded


def main():
    while True:
        print_menu()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            password = input('Please enter your password to encode:')
            print('Your password has been encoded and stored!\n')
            encoded_password = encode(password)

        elif menu_option == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the orginal password is {decoded_password}.')

        elif menu_option == 3:
            break


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
