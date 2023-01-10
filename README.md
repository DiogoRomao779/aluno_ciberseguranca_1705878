# Curso: CiberSeguranca<br />
# Disciplina: Sistemas Distribuidos<br />
![alt text](https://user-images.githubusercontent.com/113999850/191517763-9a1f1716-dc73-4ac6-9032-1e638c9f93c6.png)<br />
# Relatório do Trabalho prático<br />
# Sistemas Distribuídos<br />
# Os 100 primeiros múltiplos<br />
<br />
Aluno: <br />
Diogo Romão<br /> 
1705878<br />
<br />
https://github.com/DiogoRomao779
<br /> 
Dr3amyghost@hotmail.com
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

Resultado na consola em caso de introdução de um valor que não um inteiro.
```
C:\Users\Strix\Desktop\github_projecto\aluno_ciberseguranca_1705878\T_Practico\venv\Scripts\python.exe C:\Users\Strix\Desktop\github_projecto\aluno_ciberseguranca_1705878\T_Practico\client.py 
This program with implementation of RPC will present the first 100 multiples of an int.
Enter the int that you want, that is not 0: a
Wrong value, please try again!
Enter the int that you want, that is not 0: A
Wrong value, please try again!
Enter the int that you want, that is not 0: !
Wrong value, please try again!
```
Resultado no caso da correcta introdução de um inteiro.
```
C:\Users\Strix\Desktop\github_projecto\aluno_ciberseguranca_1705878\T_Practico\venv\Scripts\python.exe C:\Users\Strix\Desktop\github_projecto\aluno_ciberseguranca_1705878\T_Practico\client.py 
This program with implementation of RPC will present the first 100 multiples of an int.
Enter the int that you want, that is not 0: 3
3
6
9
12
15
18
21
24
27
30
33
36
39
42
45
48
51
54
57
60
63
66
69
72
75
78
81
84
87
90
93
96
99
102
105
108
111
114
117
120
123
126
129
132
135
138
141
144
147
150
153
156
159
162
165
168
171
174
177
180
183
186
189
192
195
198
201
204
207
210
213
216
219
222
225
228
231
234
237
240
243
246
249
252
255
258
261
264
267
270
273
276
279
282
285
288
291
294
297
300

['hundred', 'system.listMethods', 'system.methodHelp', 'system.methodSignature']

Process finished with exit code 0
```

## Conclusão

Considero que ao trabalho que me foi proposto pelo professor Paulo Vieira não faltou atingir qualquer objectivo, foi mencionado durante as aulas que este trabalho pode ser implementado em servidores não locais o que não acontece neste caso, mas percebendo o funcionamento e funcionalidades da arquitetura RPC, entendo o funcionamento de um servidor com múltiplas funções a receber pedidos de um cliente remoto e a respectiva entrega da resposta ao mesmo.


## 

## Bibliografia

https://www.w3schools.com/