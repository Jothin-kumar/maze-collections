from os import listdir

with open('maze/max.txt', 'w') as f:
    f.write(str(max([int(f.split('.')[0]) for f in listdir('maze') if f.endswith('.txt') and f.split('.')[0].isdigit()])))
