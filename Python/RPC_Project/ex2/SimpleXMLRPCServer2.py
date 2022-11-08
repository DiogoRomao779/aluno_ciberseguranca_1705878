from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register pow() function; this will use the value of
    # pow.__name__ as the name, which is just 'pow'.
    server.register_function(pow)

    # Register a function under a different name
    def elev_function(x, y):
        return float(x ** y)
    server.register_function(elev_function, 'elev')

    # Register an instance; all the methods of the instance are
    # published as XML-RPC methods (in this case, just 'mul').

    # Run the server's main loop
    server.serve_forever()

