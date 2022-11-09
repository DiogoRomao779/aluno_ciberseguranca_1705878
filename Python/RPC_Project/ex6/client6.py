import xmlrpc.client
s = xmlrpc.client.ServerProxy('http://localhost:8000')
x = int(input("entre o 1-valor: "))
zet = int(input("entre o zeta: "))
print(type(x))
print(s.zeta(x,zet))
# Print list of available methods
print(s.system.listMethods())