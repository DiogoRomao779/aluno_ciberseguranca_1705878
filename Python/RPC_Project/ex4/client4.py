import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
a = (input("entre o 1-valor: "))
b = (input("entre o 1-valor: "))


print(s.comp(a,b))

# Print list of available methods
print(s.system.listMethods())