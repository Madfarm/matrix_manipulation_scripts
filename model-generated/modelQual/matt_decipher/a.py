def decipher_date(encoded_date):
    # Split the encoded string into parts
    month_part, day_part, year_part = encoded_date.split()
    
    # Decode month
    month_chars = month_part.split('-')
    month = ''.join(chr(96 + int(c)) for c in month_chars)
    
    # Decode day
    day = ord(day_part) - 64
    
    # Decode year
    year_digits = []
    for char in year_part:
        if char == '#':
            year_digits.append('0')
        else:
            year_digits.append(str(ord(char.lower()) - 96))  # 'a' -> 1, 'b' -> 2, ..., 'z' -> 26
    
    year = ''.join(year_digits)
    
    return month, day, int(year)

# Example usage
encoded_date = "10-21-14-5 G B#BD"
month, day, year = decipher_date(encoded_date)
print(f"Decoded Date: {month} {day}, {year}")