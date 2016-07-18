## Problema

Em Hogwarts só existe uma quadra de Quadribol: _QPitch.py_.
Como vamos garantir que só existirá uma instância da classe
_QPitch.py_ no código pra que só dois times possam jogar de cada vez?

## Solução

Criar um ponteiro global para o objeto na primeira vez que ele for instanciado.

![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Singleton_example.png "Singleton")
