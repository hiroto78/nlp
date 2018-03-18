def cipher(data):
    ret = ""
    for char in data:
        ret += chr(219-ord(char)) if char.islower() else char
    return ret


data = 'This is a pen.'

print(cipher(data))
print(cipher(cipher(data)))
