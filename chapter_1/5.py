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


def word_bigram(words):
    ngram = []
    for i in range(len(words)):
        cw = ''
        if i >= 2 - 1:
            for j in reversed(range(2)):
                if j == 1:
                    cw += words[i-j]
                else:
                    cw += ' ' + words[i-j]
        else:
            continue
        ngram.append(cw)
    return ngram


data = 'I am an NLPer'
print(letter_bigram(data))
print(word_bigram(data.split(' ')))
