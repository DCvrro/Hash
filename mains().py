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

              
