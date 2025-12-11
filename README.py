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

#2) Sélection et affichage uniquement la colonne "longueur"
longueur = df["longueur"]
print(longueur,"\n")

# 3) filtrer les séquences dont la longueur est supérieure à 10
print("*************  Filtrage les séquences dont la longueur est  > 10 *************    ") 
filtered_df = df[df["longueur"] > 10]
print(filtered_df) 

# 4) calculer la moyenne du Pourcentage de GC 3 chiffre après la virgule 
print("****calcul de la moyenne du GC****","\n")

average_gc = df["pourcentage GC"].mean()
print(f"Pourcentage moyen de GC : {average_gc:.3f}%") 

# 5) ajouter une nouvelle colonne du catégorie de GC 
print("*****ajouter d'un nouvelle colonne *****","\n")
df["catégorie GC"] = df["pourcentage GC"].apply(lambda x: "riche" if x > 55 else "moyen " if 45 < x <= 55 else " faible ")
print(df)

# 6) ajouter une colonne donnant le nombre de'G' dans chaque séquence 
print (" ************* ajouter une colonne *************") 
df["nombre de'G' "]  =df['séquence']. apply(lambda x:  x. count('G')) 
print  (df) 

#7)calculer écart-type du Pourcentage de GC
print("************ calcul écart-type ************")

average_gc = df["pourcentage GC"].std()
print(f"pourcentage écart-type de GC: {average_gc:.5f}%")

#calculer écart-type de longueur des séquences
print("************ calcul écart-type *************")

average = df["longueur"].std()
print(f"la longueur écart-type: {average:.5f}%")
