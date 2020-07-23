import random

dict = {}
count = 0
for i in range(10000):
    int = random.randrange(30)
    if not(int in dict):
        dict[int] = 0
    if random.randrange(30) == 0:
        count += 1
    
    dict[int] +=1

print(dict)
print(count)