# %%
Mazzo = []
Semi = ['Cuori','Quadri','Picche','Fiori']
Carte = ['Asso','2','3','4','5','6','7','8','9','10','Fante','Donna','Re']

# %%
for seme in Semi:
    print(seme)

# %%
for seme in Semi:
    for carta in Carte:
        Mazzo.append( carta + ' di ' + seme)



# %%
print (Mazzo)
# %%
