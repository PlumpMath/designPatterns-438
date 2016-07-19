## Problema

Cliente precisam de uma interface simples que unifique as funcionalidades de vários sistemas complexos. No exemplo, a recepção serve de interface do banco Gringotts. OBS: nesse caso interface não significa classe abstrata, mas sim a classe que comunica diretamente com o cliente.

## Solução

Facade:
* Define nova interface (GringottsBankRecepção) que representa todos os subsistemas (GringottsBankSegurança, GringottsBankFuncionarios)
* A classe Facade deve ser Singleton, pois só pode existir uma que une os subsistemas
* Recebe ordens do cliente e delega instruções (desconhecidas pelo cliente) para os subsistemas
Assim, se o cliente quer aumentar a segurança do seu cofre, ele não precisa saber quais feitiços usarão, e nem se o Dragão será seu guardião.

![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Facade_example.png "Facade")
