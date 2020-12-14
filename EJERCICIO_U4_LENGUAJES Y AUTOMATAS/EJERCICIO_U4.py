import re

#EXPRESIONES REGULARES COMPILE
er1="\d+\s?\+\s?\d+"
er2="\d+\s?\-\s?\d+"
erd="\d+\s?\*\s?\d+"
ert="\d+\s?\/\s?\d+"
er3="[i]+\+[\+]?"
er4="\d+\.?\d+"
er5="[\+\-\*\/\%]"
er6="\=[\=]|\![\=]|\<\=?|\>\=?"
er7="assert|pass|and|as|break|class|continue|def|del|elif|else"

print("VARIABLES VÁLIDAS")
archi = 'Archivo.cs'
leer = open(archi, "r")
valida1 = re.compile(er1)
valida2 = re.compile(er2)
valida3 = re.compile(er3)
valida4 = re.compile(erd)
valida5 = re.compile(ert)
for concep in leer:
    resultado = valida1.findall(concep)
    print(resultado)
    resultado = valida2.findall(concep)
    print(resultado)
    resultado = valida3.findall(concep)
    print(resultado)
    resultado = valida4.findall(concep)
    print(resultado)
    resultado = valida5.findall(concep)
    print(resultado)
leer.close()

print("______________________________")
print("ENTEROS Y DECIMALES")
archi = 'Archivo.cs'
leer = open(archi, "r")
entdec = re.compile(er4)
for concep in leer:
    resultado = entdec.findall(concep)
    print(resultado)
leer.close()

print("______________________________")
print("OPERADORES ARITMÉTICOS")
archi = 'Archivo.cs'
leer = open(archi,"r")
opari = re.compile(er5)
for concep in leer:
    resultado = opari.findall(concep)
    print(resultado)
leer.close()

print("______________________________")
print("OPERADORES RELACIONALES")
archi = 'Archivo.cs'
leer = open(archi,"r")
opre = re.compile(er6)
for concep in leer:
    resultado = opre.findall(concep)
    print(resultado)
leer.close()

print("______________________________")
print("PALABRAS RESERVADAS")
archi = 'Archivo.cs'
leer = open(archi,"r")
pare = re.compile(er7)
for concep in leer:
    resultado = pare.findall(concep)
    print(resultado)
leer.close()




