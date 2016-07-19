## Problema

No seu sistema existe uma classe muito requisitada pelos clientes, mas o custo de instanciá-la é alto. Você só quer instanciar se o cliente realmente precisar usá-la. No exemplo, suponha que vários bruxos querem ter acesso à alma do Voldemort para destruí-la, mas ele precisaria gastar muita energia pra se proteger.

## Solução

O Proxy (Representante):
* Provê um substituto que controla acesso ao objeto real
* É uma via indireta com um nível a mais de encapsulamento entre o cliente e o objeto real
* Quando usuário puder/quiser realmente utilizar o objeto real, ele deverá ganhar acesso
<br />
No exemplo, inicialmente o bruxo tem acesso à alma do Voldemort através de sua horcruxe. No momento que ele descobre como destruí-la, a alma (objeto real) se manifesta.

![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Proxy_example.png "Proxy")
