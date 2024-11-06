"""
1. Hány negatív szám van a listában?
2. Melyik a legnagyobb szám?
3.Készíts új listát páros_lista néven, és legyenek benne a páros számok
4.Mennyi az öttel osztható számok összege?
5.Hányadik helyen áll a legkisebb szám?

"""

def negativ_szamok (lista):
    listalen = len(lista)
    negativelist = []
    for i in range(0, listalen):
        if lista[i] < 0:
            negativelist.append(lista[i])
    return negativelist

def biggestnumber (lista):
    listalen = len(lista)
    biggestnumber:int = 0
    for i in range(0, listalen):
        if lista[i] > biggestnumber:
            biggestnumber = lista[i]
    return biggestnumber

def paros_lista (lista):
    paroslista=[]
    for i in range(0, len(lista)):
        if lista[i] % 2 == 0:
            paroslista.append(lista[i])
    return paroslista

def ottel_oszthato (lista):
    ottel_oszthato=[]
    for i in range(0, len(lista)):
        if lista [i] % 5 ==0:
            ottel_oszthato.append(lista[i])
    return ottel_oszthato

def kisebbszamhelye (lista):
    kisebbszamhelye=0
    for i in range(0, len(lista)):
        if lista[i] > kisebbszamhelye:
            kisebbszamhelye=i
    return kisebbszamhelye


