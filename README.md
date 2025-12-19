# Projet-CY-antibio-tech-Sarah-doha-Gabrielle-
On étudie comment un traitement antibiotique donné à des souris au début de leur vie influence leur microbiote, en comparant un groupe traité avec un antibiotique à un groupe témoin recevant un placebo

from matplotlib import pyplot as plt
import math
import random  # <--- ajouté pour le jitter


cecal_abx = []
cecal_plb = []
ileal_abx = []
ileal_plb = []
souris_fecal = {} 


file_name = input("Please enter the file name: ")
fd = open(file_name, "r")
fd.readline()      # saute l'en-tête
line = fd.readline()

while line != '':
    line = line.replace("\n", "")
    data = line.split(";")
     
 
    nom_souris = data[4]
    traitement = data[5]
    jour = int(data[7])
    valeur = math.log10(float(data[8]) + 1)

    
    if data[2] == 'cecal':
        if traitement == 'ABX':
            cecal_abx.append(valeur)
        else:
            cecal_plb.append(valeur)
            
   
    if data[2] == 'ileal':
        if traitement == 'ABX':
            ileal_abx.append(valeur)
        else:
            ileal_plb.append(valeur)

   
    if data[2] == 'fecal':
        if nom_souris not in souris_fecal:
            # Bleu pour Placebo, Orange pour ABX
            couleur = '#ff7f0e' if traitement == 'ABX' else '#1f77b4'
            souris_fecal[nom_souris] = {'x': [], 'y': [], 'c': couleur}
        souris_fecal[nom_souris]['x'].append(jour)
        souris_fecal[nom_souris]['y'].append(valeur)
    
    line = fd.readline()
fd.close()

# GRAPHIQUE CECAL
plt.figure(figsize=(6, 5))
v = plt.violinplot([cecal_abx, cecal_plb])

# Couleurs : ABX (index 0) en orange, Placebo (index 1) en bleu
v['bodies'][0].set_facecolor('#ffcc99')
v['bodies'][1].set_facecolor('#6699ff')

# Ajout des points gris avec jitter horizontal
x_abx = [1 + random.uniform(-0.10, 0.10) for _ in cecal_abx]
x_plb = [2 + random.uniform(-0.10, 0.10) for _ in cecal_plb]
plt.scatter(x_abx, cecal_abx, color='orange', alpha=0.8, s=30, zorder=3)
plt.scatter(x_plb, cecal_plb, color='blue', alpha=0.8, s=30, zorder=3)

plt.title("Cecal live bacteria")
plt.legend(['Placebo', 'ABX'], loc='lower right')
plt.xlabel("Treatment")
plt.ylabel("log10(live bacteria/wet g)")
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.savefig("cecal_resultat.png")

# GRAPHIQUE ILEAL
plt.figure(figsize=(6, 5))
v = plt.violinplot([ileal_abx, ileal_plb])

v['bodies'][0].set_facecolor('#ffcc99')
v['bodies'][1].set_facecolor('#6699ff')

# Points avec jitter
x_abx = [1 + random.uniform(-0.08, 0.08) for _ in ileal_abx]
x_plb = [2 + random.uniform(-0.08, 0.08) for _ in ileal_plb]
plt.scatter(x_abx, ileal_abx, color='orange', alpha=0.8, s=30, zorder=3)
plt.scatter(x_plb, ileal_plb, color='blue', alpha=0.8, s=30, zorder=3)

plt.title("Ileal live bacteria")
plt.legend(['Placebo', 'ABX'], loc='lower right')
plt.xlabel("Treatment")
plt.ylabel("log10(live bacteria/wet g)")
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.savefig("ileal_resultat.png")

# GRAPHIQUE FECAL
plt.figure(figsize=(8, 6))
for nom in souris_fecal:
    infos = souris_fecal[nom]
    plt.plot(infos['x'], infos['y'], color=infos['c'], alpha=0.4)
plt.legend(['placebo', 'ABX'], loc='upper right')
plt.title("Fecal live bacteria")
plt.xlabel("washout day")
plt.grid(linestyle='--', alpha=0.3)
plt.ylabel("log10(live bacteria/wet g)")
plt.savefig("fecal_resultat.png")

plt.show()


