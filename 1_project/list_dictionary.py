def massimo(a, b):
    if(a>b):
        return 1
    elif(a<b):
        return -1
    return 0

def moltiplicatrice(lista):
    if(len(lista)):
        tot=1
        for num in lista:
            tot*=num
        return tot
    else:
        return 0

def rovescia(stringa):
    if(len(stringa)):
        stringa=stringa.capitalize()
        newString=""
        i=0
        while i<len(stringa):
            newString+=stringa[len(stringa)-1-i]
            i+=1
        return newString
    else:
        return 0

def frequenza(stringa):
    if(len(stringa)):
        d={ }
        for c in stringa:
            if(c not in d):
                dizionario[carattere]=1
            else:
                d[c]+=1
        return d
    else:
        return 0