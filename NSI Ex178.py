def occurences(t):
    occus = {}
    for x in t:
        if x in occus.keys():
            occus[x] += 1
        else:
            occus[x] = 1
            
    return occus

print(occurences("tagada"))
            
