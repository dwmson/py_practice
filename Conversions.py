## Convert between Decimal, Binary, Hexadecimal and Encode and Decode Base64
import base64

def decimal_to_binary(decimal_number):
    return bin(decimal_number)

def decimal_to_hex(decimal_number):
    return hex(decimal_number)

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def binary_to_hex(binary_string):
    decimal = int(binary_string, 2)
    return hex(decimal)

def hex_to_decimal(hex_string):
    return int(hex_string, 16)

def hex_to_binary(hex_string):
    decimal = int(hex_string, 16)
    return bin(decimal)

def encode_base64(input_string):
    return base64.b64encode(input_string.encode()).decode()

def decode_base64(base64_string):
    return base64.b64decode(base64_string).decode()

conversion_operations = {
    1: decimal_to_binary,
    2: decimal_to_hex,
    3: binary_to_decimal,
    4: binary_to_hex,
    5: hex_to_decimal,
    6: hex_to_binary,
    7: encode_base64,
    8: decode_base64
}

def converter():

    should_continue = True
    while should_continue:
        print('\nDecimal, Binary and Hex Conversion Options:')
        print('1: Decimal to Binary')
        print('2. Decimal to Hex')
        print('\n3. Binary to Decimal')
        print('4. Binary to Hex')
        print('\n5. Hex to Decimal')
        print('6. Hex to Binary')
        print('\n7. Encode to Base64')
        print('8. Decode from Base64')
        print('\n9. Exit')

        choice = int(input('Enter your choice (1-9): '))

        if choice == 9:
            break

        if choice in conversion_operations:
            if choice in [1, 2]:
                entry = int(input('Enter a number: '))
            elif choice in [3, 4]:
                entry = input('Enter a binary number: ')
            elif choice in [5, 6]:
                entry = input('Enter a hexadecimal number: ')
            elif choice in [7]:
                entry = input('Enter a string to be encoded: ')
            elif choice in [8]:
                entry = input('Enter an encoded string to be decoded: ')

            result = conversion_operations[choice](entry)
            print(f'Result: {result}')
        else:
            print('Invalid choice. Please try again')

        if input('Would you like to perform another conversion? (y/n)') == 'y':
            should_continue = False
            converter() 
        else:
            break
converter()
