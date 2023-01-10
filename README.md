<p align="center">
# aluno_ciberseguranca_1705878
Nome: Diogo Romão 1705878

Curso: CiberSeguranca

Disciplina: Sistemas Distribuidos

![alt text](https://user-images.githubusercontent.com/113999850/191517763-9a1f1716-dc73-4ac6-9032-1e638c9f93c6.png)

# Relatório do Trabalho prático<br />
# Sistemas Distribuídos<br />
<br />
<br />
## Os 100 primeiros múltiplos
<br /> 
<br />
## Aluno: 
## Diogo Romão, 
## 1705878,
<br />
## https://github.com/DiogoRomao779, 
## Dr3amyghost@hotmail.com
</p>
<br />


[**1. Descrição do Trabalho**](#descrição-do-trabalho) 

[**2. Função implementada**](#função-implementada) 

[**3. Servidor**](#servidor) 

[**4. Client**](#client) 

[**5. Funcionamento do trabalho**](#funcionamento-do-trabalho) 

[**6. Conclusão**](#conclusão) 

[**7. Bibliografia**](#bibliografia) 

## 

## Descrição do Trabalho

Neste trabalho irei implementar uma função num servidor para calcular os primeiros 100 múltiplos de um inteiro escolhido pelo cliente, devolvendo os mesmo múltiplos ao cliente, utilizando a arquitetura RPC.


## Função implementada

A função que implementei recebe um inteiro, ao receber esse inteiro se o número introduzido for 0, entra num else onde apresento um texto a explicar que 100 múltiplos de zero serão 100 zeros, caso contrário a função entra num ciclo while onde iniciou uma variável r a 0, dando o valor a essa mesma variável que será o cálculo do inteiro introduzido pelo utilizador e a variável i que será iniciada a 1 que será um counter de quantos ciclos já foram executados pelo while até ao limite de valor de i ser 100. A variável r a cada ciclo é reiniciada, não sem antes o valor da mesma ser guardado numa string para poder devolver ao utilizador. Após terminar o while é retornada a string com todos os valores de r ao longo do ciclo while.


## Servidor

```
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
           #iniciamos o i a 1 para nao termos múltiplos por 0
           i = 1
           #iniciamos a variável que será apresentada ao cliente
           texto = ''
           #ciclo while que irá calcular então os múltiplos
           while i < 101:
               r = 0
               r = x * i
               texto += str(r) + "\n"
               i += 1
           #retornamos então ao cliente o resultado que foi guardado na variável texto
           return texto

   #registo da função criada
   server.register_function(hundred_mults, 'hundred')

   #manutenção do servidor online durante tempo indefinido
   server.serve_forever()

```

## Client

```
import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8000')
#apresentação inicial
print("This program with implementation of RPC will present the first 100 multiples of an int.")
#indicamos o X como uma string com valor 0
x = '0'
#condicionamos a leitura do valor inserido pelo utilizador pedindo
#ao utilizador o tipo de valor que o programa aceita
while x == '0' or x.isnumeric() == False:
   x = (input("Enter the int that you want, that is not 0: "))
   #Fazemos a verificação do valor inserido pelo utilizador
   if x == '0' or '0' == 0 or x.isnumeric() == False:
       print("Wrong value, please try again!")
   else:
       #alteramos de string para int para efectuar pedido ao servidor
       print(s.hundred(int(x)))
       break


# Print list of available methods
print(s.system.listMethods())


```

## Funcionamento do trabalho

![](./imagens/server.PNG)

Output do server

![](./imagens/1.PNG)

Verificação de erro de divisão no cliente

![](./imagens/2.PNG)

Verificação de erro nao numerico no cliente

![](./imagens/3.PNG)

Output se é divisível

![](./imagens/4.PNG)

Output se não é divisível

## Conclusão

Considero que ao trabalho que me foi proposto pelo professor Paulo Vieira não faltou atingir qualquer objectivo, foi mencionado durante as aulas que este trabalho pode ser implementado em servidores não locais o que não acontece neste caso, mas percebendo o funcionamento e funcionalidades da arquitetura RPC, entendo o funcionamento de um servidor com múltiplas funções a receber pedidos de um cliente remoto e a respectiva entrega da resposta ao mesmo.


## 

## Bibliografia

https://www.w3schools.com/


































### 1. Descrição do Trabalho	2
### 2. Função implementada	3
### 3. Servidor	3
### 4. Client	3
### 5. Funcionamento do trabalho	3
### 6. Conclusão	3
### Bibliografia	3


























## 1. Descrição do Trabalho
// breve descrição do que consiste o trabalho

## 2. Função implementada	
  // colocar a descrição da função a implementar no servidor e explica-la 

## 3. Servidor	
// colocar o código implementado no servidor e explicá-lo

## 4. Client	
// colocar o código implementado no cliente e explicá-lo
<p>
## 5. Funcionamento do trabalho	
// colocar imagens do trabalho a funcionar e explicar

## 6. Conclusão
// descrever brevemente o que se fez e o que faltou fazer










## Bibliografia

