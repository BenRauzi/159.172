import random

list = [] 
for i in range(1000):
   list.append(random.randrange(20))

t = 0
for i in list:
    if i == 20:
        t += 1
print(t)
