def getUnicode(): # type 0 if pass without has || type 1 for hash.  
    arch = open('unicode.txt','w')
    x = 0
    while(x < 500):
        arch.write("Numero:")
        arch.write(str(x))
        arch.write("- Caracter: ")
        arch.write(str(chr(x)))
        arch.write("\n")
        x = x + 1 
    arch.close()

def getASCII(symbol):
    return ord(symbol)

def encode(string):
    size = int(len(string))

    #Listado de caracteres que no es reconocido por vsc o python. SE PROBÓ UNO POR UNO
    Null=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,
        28,29,30,31,32,33,34,60,127,128,129,143,140,145,146,147,148,149,150,151,152,153,154,155,156,157,158
        ,159,160,161,162,175,183,186,217,305,385,390,399,424,425,441,446,447,450,453]
    hash = ""
    cont = 0
    if(size < 55):
        #Veamos cuanto falta para rellenar el hash
        rest = 55 - size
        for i in range(size-1): 
            cont = getASCII(string[i]) +getASCII(string[i+1]) 
            #Al ir sumando los valores dentro del valor unicode hacemos que no se vaya escrbiiendo
            #de manera texto plano
            
            while(cont in Null): 
                cont= cont + (int(cont/7))
            hash = hash + chr(cont) #Con esto pasamos de unicode a caracter. 
        cum = getASCII(string[size-1])
    
        #Otro ciclo para rellenar
        for i in range(rest+1): #Rellenamos segun lo faltante.
            if(i%2==0):
                cum = cum + 6
                while(cum in Null):
                    cum = cum + (int(cum/7))
                hash= hash + chr(cum)

            else:
                cum = cum - 5
                if(cont <= 0):
                    cont = cont + 500

                while(cum in Null):
                    cum = cum + (int(cum/7))
                hash = hash + chr(cum)
    else: #Revisamos el caso mayor a 55
        #Si es mas largo, trabajamos en partes iguales de la misma cantidad 
        #permitida a la del hash 55.
        parts = int(size/55)
        k = 0
        l = parts*55

        for i in range(size - 1):
            if(i < l): 
                if(string[i]==' ' or string[i+1]==' '):
                    cont =7+size
                else:
                    cont = getASCII(string[i])+getASCII(string[i+1])
                if(k == parts):
                    while(cont in Null):
                        cont = cont + (int(cont/7)) 
                    hash = hash + chr(cont)
                    cont = 0 
                    k = 0
                k = k + 1
            else:
                cont = getASCII(string[i]) + int(getASCII(string[i+1])) - int(getASCII(string[i+1])/2)
                while(cont in Null): 
                    cont = cont + (int(cont/7))
        hash = hash + chr(cont)
    return hash

def writePass(text): # type 0 if pass without has || type 1 for hash.  
    with open('Resultados.txt','a', encoding="utf-8") as arch:
        arch.write('Contraseña: '+ text + '\n')
        hash = encode(text)
        arch.write('\t'+'Hash: '+ hash  + '\n' )
        arch.close()

import math as mat

def entropia(string):

    size = int(len(string))
    trpy = 0
    base = 10
    trpy = size * (mat.log(base,10))
    return trpy

import hashlib as hash
import time

def md5(string):
    code  = hash.md5(string.encode())
    ncode = code.hexdigest()
    return ncode

def sha1(string):
    code = hash.sha1(string.encode())
    ncode = code.hexdigest()
    return ncode

def sha256(string):
    code = hash.sha256(string.encode())
    ncode = code.hexdigest()
    return ncode

def leerDatos():

    arc = open("Rockyou.txt")
    lineas = arc.readlines()
    datos = list()
    
    for lineas in lineas:
        datos.append(lineas) 
    return datos

def fixArr():
    data = leerDatos()

    for i in range(0, len(data)):
        data[i] = data[i].replace('\n','')
    
    return data


def main():
    val = True 
    tmd5 = list()
    tsha1 = list()
    tsha256 = list()
    tcarro = list()
    base = list()
    while(val):
        print("Bienvenido.")
        print("¿Cuantos datos del Rockyou quiere comparar?")
        print("Ingrese la opcion que desea. (1 ,2 ,3, 4...)")
        print("1.- 1 ")
        print("2.- 10 ")
        print("3.- 20 ")
        print("4.- 50 ")
        entrada = input("5.- Salir\n")
        data = fixArr()
        if(entrada == '1'):
            base.append(data[0])

        elif(entrada == '2' ):
            for i in range(0,10):
                base.append(data[i])

        elif(entrada == '3' ):
            for i in range(0,20):
                base.append(data[i])

        elif(entrada == '4' ):
            for i in range(0,50):
                base.append(data[i])

        elif(entrada == '5'):
            break
            
        for palabras in base:
        
        ########### MD5 ###########
            inicio = time.time()
            md5(palabras)
            fin = time.time()
            tmd5.append(fin-inicio)

        ########### SHA1 ##########
            inicio = time.time()
            sha1(palabras)
            fin = time.time()
            tsha1.append(fin-inicio)
        
        ########### SHA256 ##########
            inicio = time.time()
            sha256(palabras)
            fin = time.time()
            tsha256.append(fin-inicio)
        
        ########### Carro ##########
            inicio = time.time()
            encode(palabras)
            fin = time.time()
            tcarro.append(fin-inicio)

        print("Los tiempos para realizar el hash fueron los siguientes:")
        print("MD5 :",tmd5)
        print("SHA1 :",tsha1)
        print("SHA256 :",tsha256)
        print("Carro :",tcarro)



main()