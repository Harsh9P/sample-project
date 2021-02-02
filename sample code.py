import random
randomlist = []
for i in range(0,10):
    n = random.randint(1,30)
    randomlist.append(n)
print(randomlist)

randomlist.sort()
print(randomlist)