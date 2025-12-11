#Hachemaoui aya, Master1 Microbiologie Fondamentale,09/12/2025
#Benali farah
#Ameur khouloud 
#Rabah feryal 
#Benseddik rania 

import pandas as pd

# Données : Séquence ADN, Longueur, Pourcentage GC
data ={ 
     "séquence":["ATGCGTACGTA", "GCTAGCTAGGCC", "ATGCGCGTAAGT", "TACGATCGTA", "ATGAAAGGCTT", "CGTACGTAGC", "TTAACCGGAT"],  
     "longueur":[12, 12, 12, 10, 11, 10, 10, ],
     "pourcentage GC":[50, 66.67, 58.33, 40, 45.45, 60, 50, ]
}

# Création d'un DataFrame (tableau pandas)
df = pd.DataFrame(data)
print("****************création et affichage***************** ","\n")

# Affichage du tableau
print("Tableau des séquences ADN :")
print(df)
