
from asyncore import write


def writePass(text,type): # type 0 if pass without has || type 1 for hash.  
    arch = open('Resultados.txt','a')

    if(type == 0):
        arch.write('Contraseña: '+ text + '\n') 
    elif(type == 1):
        arch.write('\t'+'Hash: '+ text  + '\n' )
    arch.close()

def getASCII(symbol):
    return ord(symbol)

def main():
    
    writePass('Hola',0)
    data = list()
    for symbol in 'hola':
        data.append(getASCII(symbol))

    #contcat = '' 
    #for val in data: 
    #    contcat = contcat + str(val) 

    contcat2 = ''
    for num in data:
        dat = bin(num)
        contcat2= contcat2 + str(dat)
    writePass(contcat2,1)

main()
