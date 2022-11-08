import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
x= int(input("entre o 1-valor: "))
y=int(input("entre o 2-valor: "))
print(type(x))

print(s.elev(x,y))


# Print list of available methods
print(s.system.listMethods())