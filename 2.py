str1 = 'パトカー'
str2 = 'タクシー'
list = []
for i, char in enumerate(str1):
    list.append(char)
    list.append(str2[i:i+1])
print(''.join(list))
