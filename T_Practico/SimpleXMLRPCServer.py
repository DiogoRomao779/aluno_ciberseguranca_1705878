from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()


    def hundred_mults(x):
        if x != 0:
            i = 1
            texto = ''
            while i < 101:
                r = 0
                r = x * i
                texto += str(r) + "\n"
                i += 1
            return texto
        else:
            return "Unless you want one hundred 0's showing on your screen I suggest you pick another number"


    server.register_function(hundred_mults, 'hundred')

    # Run the server's main loop
    server.serve_forever()
