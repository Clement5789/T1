def occurences(t):
    occus = {}
    for x in t:
        if x in occus.keys():
            occus[x] += 1
        else:
            occus[x] = 1
            
    return occus

def compare_tableaux(t ,u):
    if occurences(t) == occurences(u):
        return True
    return False
   

print(compare_tableaux([1,2,3,3,4,5,5,5], [2,1,3,3,4,5,5,5]))