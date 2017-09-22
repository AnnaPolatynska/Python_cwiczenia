# -*- coding: utf-8 -*-



""" 53  Używając serii instrukcji if, sprawdź, czy wartości od 0 do 4 są równe True lub False.  
Wykonaj 5 osobnych testów i wypisz tylko te wartości dla których konwersja daje wynik True.  """
"""liczba=input ("podaj liczbę od 0-4")
if liczba.isdigit():
        print ("podano poprawnie liczbę")
        if (int(liczba))==0:
                print ("Warunek1 jest prawdą- liczba to 0")
        if (int(liczba))==1:
                print ("Warunek2 jest prawda - liczba to 1")
        if (int(liczba))==2:
                print ("Warunek3 jest prawda - liczba to 2")
        if (int(liczba))==3:
                print ("Warunek4 jest prawda - liczba to 3")     
        if (int(liczba))==4:
                print ("Warunek5 jest prawda- liczba to 4")
else: print("dokonano złego wyboru") """

""" 54 Utwórz test korzystający z pojedynczej instrukcji if, który sprawdzi, czy podana wartość znajduje się w przedziale od 0 do 9 (włącznie z tymi wartościami).  
Wyświetl komunikat, jeśli wartość znajduje się w zadanym przedziale. Jeśli wartość nie znajduje się w zadanym przedziale wypisz komunikat: „out of range” """
"""liczba = 12
if ((liczba >=0 and liczba <=9) == True):
    print ("liczba mieści się w zakresie")
else:
    print ("out of range - liczba poza zakresem")
"""
""" 54 z wpisywaniem przez użytkownika"""
"""
liczba=input("podaj liczbę od 0 do 9")
licz=(int(liczba))
if ((licz >=0 and licz <=9) == True):
    print ("Twoja iczba to "+liczba+" liczba mieści się w zakresie")
else:
    print ("out of range - liczba poza zakresem")
"""
"""55 
Używając konstrukcji if, elseif i else utwórz test, który sprawdzi, czy wartość zmiennej znajduje, 
która się w dwóch pierwszych elementach listy i przyjmuje wartości dodatnie. 
Na zakończenie działania programu wyświetl stosowne komunikaty"""
"""list=[2,9,5]

szukaj=input ("wspisz liczbe")
print(szukaj)
a = int(szukaj)  
#rzutujesz na  int(szukaj)==list[1]): lub 
if (int(szukaj)==list[0]):
    print ("liczba jest na 1 miejscu")
elif (int(szukaj)==list[1]):
    print ("liczba jest na 2 miejscu")
 
elif (a ==list[2]):
    print ("liczba jest na 3 miejscu")
else: print ("liczba nie występuje")
"""
#56 Napisz program, który wczyta od użytkownika liczbę całkowitą i bez użycia instrukcji if wyświetli informację, czy jest to liczba parzysta, czy nieparzysta
"""liczba=input("podaj liczbę całkowitą")
if (int(liczba))%2==0:
    print ("liczba parzysta")
else: print ("liczba nieparzysta")"""
# 2 sposób 56
"""liczba =input("wpisz liczbę")
a= int(liczba)
print("liczba nieparzysta") if (a%2!=0) else print("liczba parzysta")
"""
"""#57  
Utwórz słownik zawierający jako klucze nazwy produktów znajdujących się w sklepie internetowym. 
Słownik umieść w zmiennej sklep_prod.  Wartością każdego klucza będzie opis produktu.  
Utwórz zmienną sklep_zamowienie zawierającą ciąg znaków nazwy produktu, który ktoś chce zamówić.  
Za pomocą pętli dokonaj sprawdzenia każdej pary produktów znajdujących się w sklepie internetowym z zamówieniem. 
Jeśli nazwy zostaną dopasowana wypisz stosowny komunikat. W przeciwnym razie zakomunikuj brak produktu w sklepie. """
produkty={"mleko":"krowie","maslo":"osełka","mąka":"pszenna","miód":"lipowy"}

zakup= input("czy chcesz dokonać zakupu? (tak/nie)")
a=zakup
while a == "tak":
    wybor=input("podaj produkt, który chcesz kupić: ")
    if wybor in produkty:
        print ("kupiłeś "+ wybor+ " "+produkty[wybor]+ " smacznego!")
    else: print ("brak produktu")
else: print ("koniec zakupów- zapraszamy ponownie")


#58 #Slownik.keys()   Zwraca listę kluczy w słowniku 
"""produkty={"maslo":"osełka", "jaja":"wiejskie", "pomidor":"koktajlowy"}
ilości = {"maslo":5, "jaja":30, "pomidor":50}
cena = {"maslo":7, "jaja":10, "pomidor":12}

suma=0
i="tak"
while( i=="tak"):
    zamawiam = input("podaj co chcesz zamówić? ")
    zam_ilości= int(input("podaj zamawianą ilość: "))
    if (zamawiam in produkty.keys()): 
        if(ilości[zamawiam] >= zam_ilości):
            print("Produkt dostępny: " + zamawiam)
            print("Zamawiasz: " + str(zam_ilości)+ zamawiam)
            suma += zam_ilości* cena[zamawiam]   
            ilości[zamawiam]-=zam_ilości
        elif(ilości[zamawiam] < zam_ilości):
            print("Produkt nie dostępny")
    else:
        print("Brak produktu w sklepie")        
    i = input("czy chcesz zamawiać dalej? (tak/n)")
print("Do zapłaty: "+ str(suma))
"""
"""
#P60 program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową: 
#znaki nie będące cyframi mają być ignorowane konwertujemy cyfry, nie liczby, a zatem: 911 to "dziewięć jeden jeden" 1100 to "jeden jeden zero zero. 
cyfry={1:"jeden",2:"dwa",3:"trzy",4:"cztery",5:"piec",6:"szesc", 7:"siedem", 8:"osiem", 9:"dziewiec"}

nazwy = str(input("Podaj ciąg cyfr "))
i = 0
while((i < len(nazwy)) == True):
    a = int(nazwy[i])
    print(cyfry[a])
    i += 1
"""
#P61
#end="" rzutuje na tabelę
# "\t" dodaje tabulator
"""for x in range(1,10):
    for y in range(1,10):
        print(x*y, "\t", end="")
    print()
"""
#P62
"""for x in range(3,9):
    print(x*x, "\t", end="")
    print()
    """
#P63 Wyświetl kwadraty liczb nieparzystych malejąco od 9 do 1. 
"""x=10
while x>=1:
    x-=1
    if x%%2==1:
    print(x*x, " ", end="")"""