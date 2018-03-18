import random


def text_randamize(data):
    if len(data) <= 4:
        return data
    else:
        rand = []
        for i in range(1, len(data) - 1):
            rand.append(data[i])
        ret = random.sample(rand, len(data)-2)
        ret.insert(0, data[0])
        ret.append(data[-1])
        return ''.join(ret)


data = ("I couldn't believe that I could actually understand "
        "what I was reading : the phenomenal power of the human mind .")
after_data = list(map(lambda n: text_randamize(n), data.split(' ')))
print(' '.join(after_data))
