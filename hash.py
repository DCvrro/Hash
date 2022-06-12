
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
    Null=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,
        28,29,30,31,32,33,34,129,143,146,147,148,149,150,151,152,153,154,155,156,157,158
        ,159,160,161,162,175,183,186,217,305,385,390,399,424,425,441,446,447,450,453]
    final = ""
    cont = 0
    if(size < 55):
        #Veamos cuanto falta para rellenar el hash
        rest = 55 - size
        for i in range(size-1): 
            cont = ord(string[i]) +ord(string[i+1])
            if(cont > 800): #Investigar esto.
                cont = cont - 800 
            
            while(cont in Null): 
                cont= cont + (int(cont/7))
                if(cont>800):
                    cont = cont - 800
            
            final = final + chr(cont) #Con esto pasamos de unicode a caracter. 
        cum = ord(string[size-1])
    
        #Otro ciclo para rellenar
        for i in range(rest+1): #Rellenamos segun lo faltante.
            if(i%2==0):
                cum = cum + 6
                if(cont> 800):
                    cont = cont - 800
                
                while(cum in Null):
                    cum = cum + (int(cum/7))
                final= final + chr(cum)

            else:
                cum = cum - 5
                if(cont <= 0):
                    cont = cont + 800

                while(cum in Null):
                    cum = cum + (int(cum/7))
                final = final + chr(cum)
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
                    cont = ord(string[i])+ord(string[i+1])
                if(cont > 800):
                    cont = cont - 800
                if(k == parts):
                    while(cont in Null):
                        cont = cont + (int(cont/7)) 
                    final = final + chr(cont)
                    cont = 0 
                    k = 0
                k = k + 1
            else:
                cont = ord(string[i]) + int(ord(string[i+1])) - int(ord(string[i+1])/2)
                if (cont > 800):
                    cont = cont - 800
                while(cont in Null): 
                    cont = cont + (int(cont/7))
        final = final + chr(cont)
    return final

def writePass(text): # type 0 if pass without has || type 1 for hash.  
    arch = open('Resultados.txt','a')
    arch.write('Contraseña: '+ text + '\n')
    hash = encode(text)
    arch.write('\t'+'Hash: '+ hash  + '\n' )
    arch.close()


def main():
    print("Hola")
    string = input("Ingrese string\n")
    writePass(string)
main()
