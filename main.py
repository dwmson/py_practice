# Original dictionary #
protocols_dict = {
    'FTP':['20', '21'],
    'DNS':['53'],
    'LDAP':['389'],
    'MySQL':['3306']
}

# Converts original dictionary to lower case ##
protocols_dict_lower = {key.lower(): value for key, value in protocols_dict.items()}

# Creates a reverse dictionary for port number search
ports_dict = {}
for protocol, ports in protocols_dict.items():
    for port in ports:
        ports_dict.setdefault(port, []).append(protocol)

question = input('Enter a protocol or port number: ').lower()

#Search by Protocol
if question in protocols_dict_lower:
    answers = protocols_dict_lower[question]
    print(f'The port number(s) for {question.upper()} Protocol: {", ".join(answers)}')

# Search by port number
elif question in ports_dict:
    protocol = ports_dict[question]
    print(f'The protocol for port number {question} is: {", ".join(protocol)}')

# Error message for port or protocol not found
else: 
    print(f'ERROR: The protocol or port \"{question}\" cannot be found')
