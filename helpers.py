def alphabet_position(letter):
    letter = letter.lower()   
    return alphabet.index(letter)

def rotate_character(char,rot):
    given_char =  ''
    if char.isalpha():
        new_pos = alphabet_position(char) + rot
        if new_pos < 26: 
            given_char = given_char + alphabet[new_pos]
        else: 
            given_char = given_char + alphabet[new_pos % 26] 
        if char.isupper():
            return given_char.upper()
        else:
            return given_char   
    else: 
        return char