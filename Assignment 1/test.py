import random

dict = {0:0, 1: 0, 2:0, 3:0, 4:0}

for i in range(500):
    dict[random.randint(1,4)] += 1

print(dict)