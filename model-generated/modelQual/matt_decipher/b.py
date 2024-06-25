def decipher_message(message):
    # Split the message into parts
    parts = message.split(' ')
    # Convert the first part to a month
    month = ''.join(chr(int(x) + 96) for x in parts[0].split('-'))
    # Convert the second part to a day
    day = chr(int(parts[1]) + 96)
    # Convert the third part to a year
    year = ''.join('0' if x == '#' else chr(int(x) + 96) for x in parts[2])
    # Return the deciphered message
    return f'{month} {day}, {year}'

# Test the function
message = '10-21-14-5 G B#BD'
print(decipher_message(message))