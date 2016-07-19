## Problema

Queremos emitir solicitações para um objeto sem precisar saber exatamente como ele executa essa solitação (ou até mesmo quem recebe a solicitação). No exemplo, imagine que o Harry queira enfeitiçar um bruxo. 
* O que o Harry precisa saber: nome do feitiço e, neste caso, quem é o bruxo
* O que ele não precisa saber: a física/química por trás do feitiço

## Solução

Command:
* Encapsua a solicitação em forma de objeto, permitindo a parametrização dos clientes com várias solicitações diferentes
* Uma solicitação podem ser feita, refeita e desfeita, pois é possível armazenas sua ordem de execução (i.e. usando pilha)
Fazemos cada feitiço ser uma classe que executa de fato a magia. 


![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Command_example.png "Command")
