def main():
    string = "hola"
    writePass(string)
    hash = encode(string)
    print(hash)

    for i in range(0,len(hash)):
        if(i == 51 ):
            print('Caracter:',i," - " , hash[i], "Unicode: ",ord(hash[i])  )
        if(i == 53 ):
             print('Caracter:',i," - " , hash[i], "Unicode: ",ord(hash[i])  )

def main():
    string = "hola"
    writePass(string)
    hash = encode(string)
    print(hash)

    for i in range(0,len(hash)):
        print(i ,".-" , hash[i],"\n")


def main():
    
    val = True
    while(val):
        entrada = input("Ingrese palabra: ")
        if entrada == 0:
            break
        writePass(entrada)

def main():
    val = True
    while(val):
        entrada = input("Ingrese palabra: ")
        if entrada == '0':
            val = False 
            break
        writePass(entrada)

    print("MD5:",md5('hola'))
    print("SHA1:",sha1('hola'))
    print("SHA256:",sha256('hola'))


              
