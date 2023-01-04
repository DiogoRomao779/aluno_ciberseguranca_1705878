from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Criamos o servidor
with SimpleXMLRPCServer(('localhost', 8000),
                        requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

# Definimos a função
    def hundred_mults(x):
            #iniciamos o i a 1 para nao termos multiplos por 0
            i = 1
            #iniciamos a variavel que sera apresentada ao cliente
            texto = ''
            #ciclo while que ira calcular então os multiplos
            while i < 101:
                r = 0
                r = x * i
                texto += str(r) + "\n"
                i += 1
            #returnamos entao ao cliente o resultado que foi guardado na variavel texto
            return texto

    #registo da função criada
    server.register_function(hundred_mults, 'hundred')

    #manutenção do servidor online durante tempo indefinido
    server.serve_forever()
