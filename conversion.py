BIN =       [0, 1]  #Umwandlungstabelle: Basis = Länge der Tabelle, Ort äquivalent zu dem Wert des jeweiligen Zeichen; es ist möglich mit diesem Syntax eigene Umwandlungstabellen zuschreiben
TETRA =     [0, 1, 2]
QUAD =      [0, 1, 2 ,3] 
SIX =       [0, 1, 2, 3, 4, 5]
HEPT =      [0, 1, 2, 3, 4, 5, 6]
OCT =       [0, 1, 2, 3, 4, 5, 6, 7] #Ocatal
DEC =       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] #Dezimal
DODEC =     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b'] 
HEX =       [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f'] #Hexadezimal
IKOSA =     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
IKOSAHEP =  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q']
SIXTY =     [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V','W','X']

NUMNAME =   ['Null ', 'Eins ', 'Zwei ', 'Drei ', 'Vier ', 'Fünf ', 'Sechs ', 'Sieben ', 'Acht ', 'Neun '] #es kann auch verwendet werden um bei Zahlen der selben Basis die Zeichen zu ersetzen, Diese Tabelle funktioniert nur in eine Richtung, da ein Zeichen mehr als eine Stelle hat
SPEZDODEC = ['#', ',', '+', '*', '~', '<', '>', '|', '^', '°', '}', '!']    #funktioniert als Verschlüsselung
LAMPBIN =   ['○', '●'] #Visualisierung der Bits
ARROWOCT =  ['🡪', '🡭', '🡩', '🡬', '🡨', '🡯', '🡫', '🡮']


# Funktion um zwischen beliebigen Basen umzurechen
def convert(statenamearray1, statenamearray2, inputnum):                 #Input: Array von dem System der Zahl, Array welches das Ergebins haben soll, Zukonvertriernde Zahl
    inputnum = str(inputnum)                                            #Kompabilität für Zeichen
    inputnum = list(inputnum.rstrip())                                  #Entfernt Leerzeichen, etc.
    output = []                                                         #erstellen des Array output um die append Funktion zu nutzen
    base1 = len(statenamearray1)                                        #berechnen der Ersten Basis
    base2 = len(statenamearray2)                                        #berechnen der Zweiten Basis
    for n in range(len(inputnum)):                                      #den Zeichen der Zahl dezimale Werte zuorden, indem die zukonvertriernde Zahl mit dem Ersten Array verglichen wird
        for l in range(base1):                                          
            if inputnum[n] == statenamearray1[l]:
                inputnum[n] = l
                break
    exp = len(inputnum) - 1                                             #den Höchsten Exponenten festlegen
    temp = 0                                                            #Variable temp erstellen um den += Opperator zu verwenden
    for part in range(len(inputnum)):
        inputnum[part] = int(inputnum[part])                            #die oben erstellten Zahlen in Integers umwandeln
    for n in range(len(inputnum)):                                      #die Zahl in dezimal angeben
        temp += inputnum[n]*(base1**exp)            
        exp -= 1                                                        
    inputnum = temp
    while inputnum >= 1:                                                #die Zahlen auf die neue Basis anwenden
        output.append(inputnum % base2)
        inputnum = inputnum / base2 - inputnum / base2 % 1              
    output.reverse()                                                    #durch Vereinfachung kam die umgedrehte Zahlenreihenfolge heraus
    for out in range(len(output)):                                      # Floats in Integers umwandel um sie als Index für eine Liste zuverwenden
        output[out] = int(output[out])
    for num in range(len(output)):                                      #den Zahlen die richtigen Zeichen zu ordnen
        output[num] = statenamearray2[output[num]]
    temp = ''                                                           #temp als String definieren um später den += Operator zu verwenden
    for t in range(len(output)):                                        #output von Liste zu String konvertrieren
        temp += str(output[t])
    output = temp
    return output


# Funktion beliebigen Basen in Dezimal umzurechen
def converttodec(statenamearray1, inputnum):                             #wie die erste Hälfte von convert()
    inputnum = str(inputnum)
    inputnum = list(inputnum.rstrip())
    base1 = len(statenamearray1)
    for n in range(len(inputnum)):
        for l in range(base1):
            if inputnum[n] == statenamearray1[l]:
                inputnum[n] = l
                break
    exp = len(inputnum) - 1
    temp = 0
    for part in range(len(inputnum)):
        inputnum[part] = int(inputnum[part])
    for n in range(len(inputnum)):
        temp += inputnum[n]*(base1**exp)
        exp -= 1
    inputnum = temp
    return inputnum


alphabetlow = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabetup =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


# Funktion um alle Buchstaben um eine wert zu verschieben
def caesar(shift, text):
    output = ''                                                 #output deklarien um += verwenden zu können
    text = list(str(text))                                      #text in Liste umwandeln
    shift = shift%26                                            #Caesar Code ist periodisch, deshalb braucht man nur den modulo
    negshift = 26 - shift                                       #falls man einmal über z heraus kommt kann man auch rückwärts gehen
    for n in range(len(text)):
        if text[n].islower():                                   #Schleife um Kleinbuchstaben zu verschieben
            for m in range(26):
                if text[n] == alphabetlow[m]:                   #Wert des Zeichen finden
                    marker = m
                    break
                else:                                           #Fall für alle Sonderzeichen
                    marker = None
            if marker != None:                                  #startet nur wenn das Zeichen kein Sonderzeichen ist
                try:                                            #erst positiv verschieben
                    text[n] = alphabetlow[marker + shift]
                except IndexError:                              #negativ verschieben wenn positiv nicht funktioniert
                    text[n] = alphabetlow[marker - negshift]
        elif text[n].isupper():                                 
            for m in range(26):                                 #Schleife um Großbuchstaben zu verschieben, gleich wie oben
                if text[n] == alphabetup[m]:
                    marker = m
                    break
                else:
                    marker = None
            if marker != None:
                try:
                    text[n] = alphabetup[marker + shift]
                except IndexError:
                    text[n] = alphabetup[marker - negshift]
    for n in range(len(text)):
        output += text[n]                                       #zusammenfügen des Texts
    return output


# Funktion um alle Buchstaben um eins zu verschieben
def caesarone(text):                                            #gleich wie caesar() nur die verschiebung ist auf 1 fest gelegt
    output = ''
    text = list(str(text))
    for n in range(len(text)):
        n = n
        if text[n].islower():
            for m in range(26):
                if text[n] == alphabetlow[m]:
                    marker = m
                    break
                else:
                    marker = None
            if marker != None:
                try:
                    text[n] = alphabetlow[marker + 1]
                except IndexError:
                    text[n] = alphabetlow[marker - 25]
        elif text[n].isupper():
            for m in range(26):
                if text[n] == alphabetup[m]:
                    marker = m
                    break
                else:
                    marker = None
            if marker != None:
                try:
                    text[n] = alphabetup[marker + 1]
                except IndexError:
                    text[n] = alphabetup[marker - 25]
    for n in range(len(text)):
        output += text[n]
    return output


ZEICHENLANG = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'V̅', 'X̅', 'L̅', 'C̅', 'D̅', 'M̅'] #maxvalue = 3999999
ZEICHEN = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
CUSTOMZEICHEN = []
ZEICHENSATZ = ['I', 'V', 'X', 'L', 'C', 'D', 'M', 'V̅', 'X̅', 'L̅', 'C̅', 'D̅', 'M̅']


#Funktion um Zeichensatz auszuwählen für römische Zahlen
def selectroman(ZEICHENSATZ):
    if ZEICHENSATZ == 'long':
        ZEICHENSATZ = ZEICHENLANG
    elif ZEICHENSATZ == 'custom':
        ZEICHENSATZ = CUSTOMZEICHEN
    else:
        ZEICHENSATZ = ZEICHEN


#Funktion um int in römische Zahlen umzuwandeln
def romannumber(number):        
    try:                                                                                        #testet den Input
        number = int(number) 
    except ValueError: 
        return ValueError                                           
    maxvalue = len(ZEICHENSATZ)                                                                 #berechnet die maximale darstellbare Zahl
    maxvalue = maxvalue / 2 + 1 - maxvalue / 2 % 1 
    maxvalue -= 1 
    if len(ZEICHENSATZ) % 2 != 0:  
        maxvalue = 4 * 10 ** maxvalue - 1                                                       #teste für alle ungeraden Längen des Array
    else:
        maxvalue = 9 * 10 ** maxvalue - 1                                                       #teste für alle geraden Längen des Array
    if number > maxvalue:                                                                       #sortiert nich darstellbare Zahlen aus
        return OverflowError            
    number = list(str(number))                                                                  #Macht aus einer Zahl eine Liste
    number.reverse()
    for f in range(len(number)):                                                                #Zahl wird umgedreht für leichteren Umgang mit Array
        number[f] = int(number[f])
    for a in range(len(number)):                                                                #ordnet jeder Zahl des Arrays sein Zeichen zu
        temp = ''
        if number[a] <= 3:                                                                      #die Zahlen 0-3 sind gleich auf gebaut: I,II,III
            for _b in range(number[a]):
                temp += ZEICHENSATZ[a * 2]                                                  
        elif number[a] == 4:                                                                    #die Zahl 4 ist ein Sonderfall: IV
            temp = ZEICHENSATZ[a * 2] + ZEICHENSATZ[(a * 2) + 1]
        elif number[a] > 4 and 9 > number[a]:                                                   #die Zahlen 5 bis 8 sind gleich aufgebaut: V,VI,VII,VIII
            temp = ZEICHENSATZ[(a * 2) + 1]
            for _c in range(number[a]-5):
                temp += ZEICHENSATZ[a * 2]                                                   
        elif number[a] == 9:                                                                    #9 ist wieder ein sonderfall
            temp = ZEICHENSATZ[a * 2] + ZEICHENSATZ[(a * 2) + 2]
        number[a] = temp
    number.reverse()                                                                            #Zahl wird wieder umgedreht
    temp = ''
    for n in number:                                                                            #die Zahl wird Zusammengefügt
        temp += n
    number = temp
    return number


Zahlenwörter = ['', 'tausend', 'Million', 'Milliard', 'Billion', 'Billiard', 'Trillion', 'Trilliard', 'Quadrillion', 'Quadrilliard', 'Quintillion', 'Quintilliard',
                'Sextillion', 'Sextilliard', 'Septillion', 'Septilliard', 'Oktillion', 'Oktilliard', 'Nonillion', 'Nonilliard', 'Dezillion', 'Dezilliard']                      # wer mehr will kann gerne ergänzen https://de.wikipedia.org/wiki/Zahlennamen
Zahlen = ['', 'ein', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf','dreizehn','vierzehn','fünfzehn','sechzehn','siebzehn']
Zehner = ['','zehn','zwanzig','dreißig','vierzig','fünfzig', 'sechzig', 'siebzig', 'achtzig','neunzig']
maxnum = 10**(3*len(Zahlenwörter))-1


#Funktion um Zahlen auszuschreiben
def zzw(number):
    zahl = ''
    oneflag =[]
    try:
        number = int(number)
    except ValueError:
        return ValueError
    höchst = 10**(len(Zahlenwörter)*3)
    if number == 0:
        return 'null'
    elif number == 1:
        return 'eins'
    elif number % höchst != number:
        return IndexError
    else:
        läng = len(str(number))
        hunderter = []
        for l in range(max(int(läng / 3 +(1- läng / 3%1)), 1)):                         
            temporär = number % 10 ** ((l + 1) * 3) - number % 10 ** (max(l, 0) * 3)
            temporär = temporär / 10 ** (max(l, 0) * 3)
            if temporär != 0:
                hunderter.append(int(temporär))
        hunderter.reverse()
        for k in range(len(hunderter)):
            if (hunderter[k] / 10 - hunderter[k] / 10 % 1) % 10 == 0 and hunderter[k]%10 == 1:
                oneflag.append(1)
            else:
                oneflag.append(0)
        for o in range(len(hunderter)):
            hunderter[o] = namehunderter(hunderter[o])
        for h in range(len(hunderter)):
            antih = len(hunderter) - h - 1
            if antih > 1 and oneflag[h] == 0:
                zahl += hunderter[h] + ' ' + Zahlenwörter[antih]
                if antih % 2 == 1:
                    zahl += 'en'
                zahl += ' '
            elif antih > 1 and oneflag[h] == 1:
                zahl += hunderter[h] + 'e ' + Zahlenwörter[antih]
                if antih % 2 == 1:
                    zahl += 'e'
                zahl += ' '
            elif antih == 1 :
                zahl += hunderter[h] + 'tausend'
            elif antih < 1 and oneflag[h] == 0:
                zahl += hunderter[h]
            elif antih < 1 and oneflag[h] == 1:
                zahl += hunderter[h] + 's'
        return zahl


# Funktion um Zahlen bis 999 auszuschreiben
def namehunderter(number):                  
    if number % 1000 != number:
        return IndexError
    if number % 100 == number:
        number = str(number)
        while len(number)<3:
            number = '0' + number
    final = ''
    number = list(str(number))
    for m in range(len(number)):
        number[m] = int(number[m])
    if number[0] != 0:
        final += Zahlen[number[0]]
        final += 'hundert'
    if number[1] == 0:
        final += Zahlen[number[2]]
        return final
    elif number[1] < 2 and number[2] < 8:
        final += Zahlen[int(number[1]*10+number[2])] 
        return final
    elif number[1] == 1 and number[2] > 7:
        final += Zahlen[number[2]]
        final += Zehner[number[1]]
        return final
    elif number[1] > 1:
        if number[2] != 0:
            final += Zahlen[number[2]]
            final += 'und'
        final += Zehner[number[1]]
        return final


def intlen(integer):
    ten = 10
    length = 1
    while integer % ten != integer:
        length += 1
        ten = 10 ** length
    return length


def sgn(num):
    return num / abs(num)

