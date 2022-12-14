import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
print("This program with implementation of RPC will present the first 100 multiples of an int.")
x = int(input("enter the int that you want: "))

print(s.hundred(x))

# Print list of available methods
print(s.system.listMethods())
