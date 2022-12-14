import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print("Este programa com implementação RPC irá apresentar os 100 primeiros multiplos de um inteiro.")
x = int(input("intruduza o inteiro que pretende: "))

print(s.hundred(x))

# Print list of available methods
print(s.system.listMethods())
