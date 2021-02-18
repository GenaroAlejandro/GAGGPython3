import re

def valcorreo(correo):
    #Patrón general = <nombre> + <@> + <curso> + <.> + <python> + <.> + <mx>
    patron1 = '(([A-Z])|([a-z])).*@{1}' #Para asegurar que comience con letra may o min (en metodo match)
    patron2 = '\.'
    patron3 = '(?<=(@curso.python.m))x'
    patron4 = 'mx$'
    p1 = re.match(patron1,correo)
    p2 = re.search(patron2,correo)
    p3 = re.search(patron3, correo)
    p4 = re.search(patron4, correo)
    if(p1 and p2 and p3 and p4):
        print('Correo valido')
        return True

def valcurp(curp):
    """
    patron general: <caracter alfanumerico> + <Vocal> <2Caracteres alfanumericos> ...
    ... + <2Digitos: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11 o 12> ...
    ... + <2Digitos: 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11 o 12, 13, 14, 15, 16, 17, 18, 19, 20, 21 o 22, 23, 24, 25, 26, 27, 28, 29, 30 o 31> ...
    ... + <caracter H o M> + <2Caracteres alfanumericos predefinidos (del estado)> ...
    ... + <3Consonantes> + <Digito o caracter alfanumerico> + <Digito al final>
    """
    patron = '[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])[HM]{1}(AS|BC|BS|CC|CS|CH|CL|CM|DF|DG|GT|GR|HG|JC|MC|MN|MS|NT|NL|OC|PL|QT|QR|SP|SL|SR|TC|TS|TL|VZ|YN|ZS|NE)[B-DF-HJ-NP-TV-Z]{3}[0-9A-Z]{1}[0-9]{1}$'
    p = re.match(patron,curp)
    if(p):
        print('Curp valida')
        return True

def valcelular(numero):
    patron1 = '[0-9]{10}'
    patron2 = '\([0-9]{2}\)[0-9]{8}'
    patron3 = '\([0-9]{3}\)[0-9]{7}'
    patron4 = '\([0-9]{2}\) [0-9]{4} [0-9]{4}'
    patron5 = '\([0-9]{3}\) [0-9]{3}-[0-9]{4}'
    p1 = re.match(patron1, numero)
    p2 = re.match(patron2, numero)
    p3 = re.match(patron3, numero)
    p4 = re.match(patron4, numero)
    p5 = re.match(patron5, numero)
    if (p1 or p2 or p3 or p4 or p5):
        print('numero valido')
        return True



if __name__ == '__main__':
    print('Ingrese su correo:')
    correo = input()
    print('Ingrese su CURP:')
    curp = input()
    print('Ingrese su numero:')
    cel = input()
    Correo = valcorreo(correo)
    Curp = valcurp(curp)
    Cel = valcelular(cel)


