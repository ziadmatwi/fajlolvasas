import fajlkezeles
import feladatok
lista=fajlkezeles.fajlbol_olvas()

negativlista=feladatok.negativ_szamok(lista)
print(negativlista)

biggestnumber=feladatok.biggestnumber(lista)
print(biggestnumber)

paroslista=feladatok.paros_lista(lista)
print(paroslista)

ottel_oszthato=feladatok.ottel_oszthato(lista)
print(ottel_oszthato)

kisebbszamhelye=feladatok.kisebbszamhelye(lista)
print(kisebbszamhelye)

