def letter_bigram(words):
    ngram = []
    for i in range(len(words)):
        cw = ''
        if i >= 2 - 1:
            for j in reversed(range(2)):
                cw += words[i-j]
        else:
            continue
        ngram.append(cw)
    return ngram


data1 = 'paraparaparadise'
data2 = 'paragraph'

X = letter_bigram(data1)
Y = letter_bigram(data2)
print(X)
print(Y)

# union
print('union')
union = list(filter(lambda n: n in X, Y))
print(union)

# intersection
# difference
