import random  

# Générer un nombre aléatoire entre 1 et 100  
nombre_magic = random.randint(1, 100)  

# Demander à l'utilisateur de saisir un nombre  
nombre_utilisateur = int(input("Veuillez entrer un nombre entre 1 et 100 : "))  

# Vérifier si le nombre de l'utilisateur est égal, supérieur ou inférieur au nombre magique  
if nombre_utilisateur == nombre_magic:  
    print("Félicitations ! Vous avez trouvé le nombre magique qui est", nombre_magic)  
elif nombre_utilisateur < nombre_magic:  
    print("Le nombre magique est supérieur à votre nombre. Il est", nombre_magic)  
else:  
    print("Le nombre magique est inférieur à votre nombre. Il est", nombre_magic)