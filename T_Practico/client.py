import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print("This program with implementation of RPC will present the first 100 multiples of an int.")
x = '0'
while x == '0' or x.isnumeric() == False:
    x = (input("Enter the int that you want, that is not 0: "))
    if x == '0' or '0' == 0 or x.isnumeric() == False:
        print("Wrong value, please try again!")
    else:
        # importante fazer cast para int
        print(s.hundred(int(x)))
        break


# Print list of available methods
print(s.system.listMethods())

