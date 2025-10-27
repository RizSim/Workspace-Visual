
# %%
import random

NumGiocatori = int(input('Quanti Giocatori ? '))

NomeGiocatori=[]

for x in range(NumGiocatori):
    NomeGiocatori.append(input('Nome'))


# %%
Mazzo = []
Dorso =['Blu','Rosso']
Semi = ['Cuori','Quadri','Picche','Fiori']
Carte = ['Asso','2','3','4','5','6','7','8','9','10','Fante','Donna','Re']

# %%
for seme in Semi:
    print(seme)

# %%
for col in Dorso:
    for seme in Semi:
        for carta in Carte:
            Mazzo.append( carta + ' di ' + seme +' ' + col)
    Mazzo.append ('Jolly Nero ' + col)
    Mazzo.append ('Jolly Rosso ' + col)
# %%
print (Mazzo)

# %%
random.shuffle(Mazzo)

# %%

for x in range(10):
    for Nome in NomeGiocatori:
        Nome[0].append(Mazzo[x].pop)
# %%
