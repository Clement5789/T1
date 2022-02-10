import random

def doublon(t):
    et = set()
    for x in t:
        if x in et:
            return True
        else:
            et.add(x)
    return False

coincid = 0

for i in range(1000):
    anivs = [random.randint(1, 365) for j in range(23)]
    if doublon(anivs):
        coincid += 1
        
print(coincid)