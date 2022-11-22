from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    def div_function(x,y):
        if y != 0:

            return float (x/y)
        else:
            return "dividing by 0 will make you enter in a timelapse"


    server.register_function(div_function, 'div')



    # Run the server's main loop
    server.serve_forever()

