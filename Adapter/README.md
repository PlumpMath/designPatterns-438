## Problema

Você descobriu que já possui uma classe que faz tudo o que você precisa. O problema é que a interface dela não é compatível sua arquitetura sendo desenvolvida (por exemplo, seu construtor requer 4 parâmetros, mas você só precisa passar 2). No exemplo do diagrama, a FamiliaTrouxa teve um filho bruxo de sangue ruim, mas ela esperava um FilhoTrouxa.

## Solução

O nome da gambiarra é Adapter, que:
* Converte a interface da classe antiga para uma que encaixa nos requisitos do cliente
* "Cobre" a classe antiga com uma interface nova
* Promove o reuso de classes antigas
A classe FilhoSangueRuim vai fazer a conexão: brincar significará voar de vassoura e estudar significará enfeitiçar.

![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Adapter_example.png "Adapter")
