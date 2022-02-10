AZERTY = ["azertyuiop",
          "qsdfghjklm",
          "<wxcvbn,;:"]

def inverse_clavier(t):
    dico = {}
    for i in range(len(AZERTY)):
        for j in range(len(t[0])):
            dico[t[i][j]] = (j, i)
            
    print(dico)
    
inverse_clavier(AZERTY)

def distance_touches(a, b):
    dico = inverse_clavier(AZERTY)
    dist = ((dico[b][0] - dico[a][0])**2 + (dico[b][1] - dico[a][1])**2)**0.5
    
    return dist

print(distance_touches("a", "s"))