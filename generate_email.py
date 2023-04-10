import random

# Ouvrir le fichier contenant la liste de noms
with open("user.txt", "r") as f:
    noms = f.readlines()

# Générer une liste de nombres aléatoires
nombres = [random.randint(10000000, 10000000000) for _ in range(len(noms))]

# Écrire les noms avec les nombres aléatoires dans un nouveau fichier
with open("mail.txt", "w") as f:
    for nom, nombre in zip(noms, nombres):
        f.write(f"{nom.strip()}{nombre}\n")

with open("fnac_mail.txt", "w") as f:
    for nom, nombre in zip(noms, nombres):
        f.write(f"{nom.strip()}{nombre}@yopmail.com\n")
