def plus_frequent(d, k):
    best = 0
    best_key = ""
    
    for key in d.keys():
        if len(key) == k:
            if d[key] > best:
                best_key = key
                best = d[key]
                
    return best_key
        
dico = {"pop": 20, "toto": 50, "titi": 40, "tut": 20}

print(plus_frequent(dico, 4))