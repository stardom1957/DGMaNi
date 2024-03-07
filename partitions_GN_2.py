# Chap 7 de Data Structures & Algorithms in Python
# Expérimentation pour ma compréhension des Partitions
# GN : 2024-02-28 : 2024-03-02 : partitions_GN v1.3

import random

N=18                # Nombre d'items dans la liste
M=100                # Valeur maximale pour un item

def montrePart(liste,bas=None,haut=None,pivot=None):
    vide='  '
    if bas+1 == haut:
        c0='   ┌'+'─'*((bas+1)*5-1)+'┬'+'─'*((N-haut)*5-1)+'┐'
    else:
        c0='   ┌'+'─'*((bas+1)*5-1)+'┐'+' '*((haut-bas-1)*5-1)+'┌'+'─'*((N-haut)*5-1)+'┐'
    c1='  │'
    if bas+1 == haut:
        c2='   └'+'─'*((bas+1)*5-1)+'┴'+'─'*((N-haut)*5-1)+'┘'
    else:
        c2='   └'+'─'*((bas+1)*5-1)+'┘'+' '*((haut-bas-1)*5-1)+'└'+'─'*((N-haut)*5-1)+'┘'

    print(c0)
    print('   │',end='')
    for i in range(len(liste)):
        if ((i == bas) or (i== haut)):
            if i == bas:
                print(f'[{l[i]:2}]│',end='')     # Affiche le bas actuel et la limite finale basse
            else:
                print(f'\b│[{l[i]:2}] ',end='')  # Affiche le haut actuel et la limite initiale haute
        else:
            if ((i == bas+1) and (i != haut)):
                print(f'{l[i]:3} ',end=' ')
            else:
                print(f'{l[i]:3} ',end=' ')
    print(f'\b│ : ',f'{bas:2}',f'{haut:2}',f'{pivot:2}')
    print(c2)

# Création d'une liste de nombres aléatoires
l=[]
for i in range(N):
    l.append(random.randrange(M))

# print(l)
b=0
h=len(l)-1
#p=5
#p=random.randrange(int(M/4),int(M/4)*3)
#p=int(N/2)
#p=int((l[p]+l[p+1])/2)

t=0
for i in l:
    t+=i
p=int(t/len(l))

# Affichage de la liste originale
print('Liste originale :')
print('  ',end='')
for i in range(len(l)):
    print(f'{l[i]:5}',end='')
print()

# Affichage de l'étape 0 du partitionnement
etape=0
while (b<h):
    print('Étape',etape)
    if etape == 0:
# L'étape 0 montre l'état de départ de la liste avec les deux partitions vides
        ab=b    # ancien bas
        ah=h    # ancien haut
        print(' ┌┐'+' '*((h-b)*5+5)+'┌┐')
        print(' ││',end='')
        for i in range(len(l)):
            if ((i == b) or (i== h)):
                print(f' [{l[i]:2}] ',end='')    # Affiche le bas et le haut actuels
            else:
                if ((i == b+1) and (i != h)):
                    print(f'{ l[i]:3}',end=' ')
                else:
                    print(f'{ l[i]:4}',end=' ')

        while ((b<h) and (l[b]<p)):
            b+=1
        while ((b<h) and (l[h]>=p)):
            h-=1
        l[b],l[h] = l[h], l[b]
        etape+=1
        print('\b││')
        print(' └┘'+' '*((ah-ab)*5+5)+'└┘')

    else:
        montrePart(l,b,h,p)
        while ((b<h) and (l[b]<p)):
            b+=1
        while ((b<h) and (l[h]>=p)):
            h-=1
        l[b],l[h] = l[h], l[b]
        etape+=1

print('Fin :')
c='   ┌───'+'─'*((b-1)*5+0)+'─┬─'+'─'*((N-1-h)*5+1)+'──┐'
print(c)

print('   │',end='')        # Début de partition (ligne 2)
for i in range(len(l)):
    if i == b:
        print('\b│',end='')
        print(f'{l[i]:3}  ',end='') # Affichage de la partition haute
    else:
        print(f'{l[i]:3}  ',end='') # Affichage de la partition basse
print('\b│')
# print('12341234123412341234123412341234123412341234123412341234123412341234')
c='   └───'+'─'*((b-1)*5+0)+'─┴─'+'─'*((N-1-h)*5+1)+'──┘'
print(c)
print('  ',end='')
for i in range(len(l)):
    print(f'{i:5}',end='')
print()
print('bas=[',0,'-',b-1,']','haut=[',h,'-',N-1,'] pivot =', p)

