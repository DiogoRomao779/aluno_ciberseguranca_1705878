import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
#apresentação inicial
print("This program with implementation of RPC will present the first 100 multiples of an int.")
#indicamos o X como uma string com valor 0
x = '0'
#condicionamos a leitura do valor inserido pelo utilizador pedindo
#ao utilizador o tipo de valor que o programa aceita
while x == '0' or x.isnumeric() == False:
    x = (input("Enter the int that you want, that is not 0: "))
    #Fazemos a verificação do valor inserido pelo utilizador
    if x == '0' or '0' == 0 or x.isnumeric() == False:
        print("Wrong value, please try again!")
    else:
        #alteramos de string para int para efectuar pedido ao servidor
        print(s.hundred(int(x)))
        break


# Print list of available methods
print(s.system.listMethods())

