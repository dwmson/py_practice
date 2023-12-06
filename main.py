# Original dictionary ##
protocols_dict = {
    'FTP':'21',
    'DNS':'53',
    'LDAP':'389',
    'MySQL':'3306'
}

# Converts original dictionary to lower case ##
protocols_dict_lower = {key.lower(): value for key, value in protocols_dict.items()}

# Creates a reverse dictionary for port number search
ports_dict = {value: key for key, value in protocols_dict.items()}

question = input('Enter a protocol or port number: ').lower()

#Search by Protocol
if question in protocols_dict_lower:
    answer = protocols_dict_lower[question]
    original_key = [key for key, value in protocols_dict.items() if value == answer][0]
    print(f'The port number for protocol {original_key} is {answer}.')

# Search by port number
elif question in ports_dict:
    protocol = ports_dict[question]
    print(f'The protocol for port number {question} is {protocol}')

# Error message for port or protocol not found
else: 
    print(f'ERROR: The protocol or port \"{question}\" cannot be found')
