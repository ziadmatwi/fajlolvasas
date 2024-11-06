import random

def lista_letrehozasa():
    #generálj 100 véletlen egész számot [-50,150] között
    # a függvény térjen vissza a listával
    list:float=[]
    i:int=1
    a:float=0
    while i <= 100:
        a=int(random.random()*(151+50)-50)
        list.append(a)
        i+=1
    return list


# a listában lévő számokat fűzd össze stringgé, az elválasztó jel ; legyen
#az utolsó után ne legyen ;


def szovegge_alakit(lista):
    szoveg:str=""
    for i in range (0, len(lista),1):
        if (i<len(lista)-1):
            szoveg+=f"{lista[i]}; "
        else:
            szoveg+=f"{lista[i]}"
    print (szoveg)   
    return szoveg

def fajlba_mentes(szoveg):
    fajlom = open("adatok.txt", "w", encoding='utf-8')
    fajlom.write(szoveg)
    fajlom.close()

def fajlbol_olvas():
    fajlom = open("adatok.txt", "r", encoding='utf-8')
    szoveg_fajlbol:str=fajlom.read()
    szoveg_lista=szoveg_fajlbol.split(";")
    lista=[]
    for i in range(0, len(szoveg_lista), 1):
        szam:int= int(szoveg_lista[i].strip())
        lista.append(szam)
    fajlom.close()
    return lista


   