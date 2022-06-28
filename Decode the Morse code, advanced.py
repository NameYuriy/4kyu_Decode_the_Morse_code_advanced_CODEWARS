def decode_bits(bits):
    bits_copy = bits
    if bits_copy[0] == '0':
        i = 1
        while bits_copy[i-1] == '0':
            i+=1
        bits_copy = bits_copy.strip('0'*i).rstrip('0'*i)
    if bits_copy.find('1') != -1 and bits_copy.find('0') != -1:
        bits_min_0 = sorted([len(k) for k in bits_copy.split('1') if k !=''])[0]
        bits_min_1 = sorted([len(k) for k in bits_copy.split('0') if k !=''])[0]
        min_ = (bits_min_0 if bits_min_0<=bits_min_1 else bits_min_1)
        if min_%9 == 0:
            speed = min_/3
        else:
            speed = min_
    elif bits_copy.find('1') == -1:
        return ''
    elif bits_copy.find('0') == -1:
        return '.'
    return bits_copy.replace('111'*int(speed), '-').replace('000'*int(speed), ' ').replace('1'*int(speed), '.').replace('0'*int(speed), '')

def decode_morse(morseCode):
    words = ''
    morseCode = morseCode.split(' ')
    keys = dict.keys(MORSE_CODE)
    for letter in morseCode:
        if letter in keys and letter != '':
            words += MORSE_CODE[letter]
        elif letter == '':
            words += ' '
    return words
