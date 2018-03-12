import re

data = ('Now I need a drink, alcoholic of course, '
        'after the heavy lectures involving quantum mechanics.')
print(list(map(lambda x: len(re.sub('[,.]', '', x)), data.split(' '))))
