## Problema

Define uma dependência de um (centro observatório) para muitos (observadores) para que quando o objeto observado mude seu estado, essa informação seja transmitida à todos os observadores. No mundo do bruxos, é necessário URGENTE uma solução para isso: eles não usam televisão nem internet, a comunicação é feita por corujas, etc.

## Solução

* Define uma dependência de um (observatório) para muitos (observadores) para que quando o objeto observado mude seu estado, essa informação seja transmitida à todos os observadores
* Objeto observado tem seus observadores encapsulados pelo observatório
* É o "View" da arquitetura MVC (Model-View-Controller)
<br />
Para amenizar o problema de comunicação em Hogwarts, criamos no exemplo um "ObservadorDeAmpulhetas" que atualiza a casa de maior pontuação (pode ser através de rádio) para os membros da escola sempre que um Adm mudar seu estado.

![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Observer_example.png "Observer")
