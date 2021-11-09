UESC, Redes 1, Victor Martins

* Instruções

Primeiro execute o socket: servidor.py, servidor ficará esperando o estabelecimento de conexão.

Execute o socket: cliente.py, conectará ao servidor.

Envie uma mensagem qualquer.

* Comandos úteis:

servidor_Socke.py

	chmod 744 servidor.py
	./servidor_Socke.py
	
cliente_socke.py

	chmod 744 cliente.py
	./cliente_socke.py


* Teoria

A principio o servidor especificará o socket(TCP/UDP) e tipo de endereço(IPV4/IPV6).

	serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Seguidamente, é necessário vincular o IP a porta com método bind.
   
   	serv_socket.bind(addr)

Servidor entra em modo de espera/escuta
   	
   	serv_socket.listen(3)

Quando requisitado conexão, será aceita.

   	conn, cliente = serv_socket.accept()

O socket para o cliente(Criar)
   
   	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Solicitação de conexão com o servidor
   
   	client_socket.connect_ex(addr)

Cliente envia dados
   
   	client_socket.sendall(str.encode(mensagem))

Servidor lê os bytes até um tamanho definido
   
   	data = conn.recv(1024)

Devolve dados para o cliente
   
   	conn.sendall(data)

O cliente Lê os bytes até um tamanho definido
   
   	data = client_socket.recv(1024)

Servidor termina a conexão
   	
   	conn.close()


Propósito do software, motivação da escolha do protocolo de transporte e os requisitos mínimos de funcionamento

Os Sockets são empregados para o envio de mensagens através de uma rede. São uma das formas mais comum de IPC -Inter-Process Communication.As aplicações mais comuns para sockets são aplicações cliente-servidor, nas quais um servidor espera por conexões de clientes. Nesse caso, será  criado um socket tcp, pois com o socket tcp os dados são enviados sem erros ou duplicação, e recebidos na mesma ordem em que foram enviados.
Para que a comunicação aconteça, é necessário ter um serviço com o papel de servidor e outro com o papel do cliente. O servidor deve ficar ouvindo, ou seja, no estado de aguardo por alguma solicitação de clientes que desejam se comunicar. E o cliente será o responsável por iniciar a comunicação com o servidor. Dessa forma, é possível notar que um dos requisitos mínimos para estabelecer uma comunicação é ter um servidor, esperando por uma solicitação de comunicação e um cliente para iniciar a comunicação.


Protocolo da camada de aplicação HTTP

O HTTP - protocolo de transferência de hipertexto é um protocolo da camada de aplicação, responsável pela transmissão de documentos de hipermídia, como o HTML. Sempre que você abre o seu navegador e digita o endereço de alguma página Web, por exemplo: (wwww.google.com.br), um Socket é criado pelo navegador. Neste caso, você é o Cliente e o computador em que a página Web está armazenada é o Servidor. Nesse contexto, o usuário final (você) não tem ciência de um conjunto de etapas que ocorre internamente dentro do sistema operacional (Windows/Linux/Mac) do Servidor e do Cliente.  No nível da camada de aplicação, geralmente o navegador faz uma comunicação usando o protocolo HTTP ou HTTPS. Estes permitem a obtenção de recursos, tais como documentos HTML que são a base de toda página Web. Neste ponto, é importante dizer que cada protocolo da camada de aplicação tem associado a ele uma porta padrão de operação, no caso do protocolo HTTP a porta 80 é o padrão universal, no HTTPS temos a porta 443, o FTP tem a porta 23, etc. Na sequência (Camada de Transporte), escolhe-se como a comunicação irá tratar a entrega de dados. Neste caso, se usar TCP temos a garantia de que nenhuma parte dos dados transmitidos serão perdidos.

















