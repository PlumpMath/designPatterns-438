## Problema

O sistema precisa de uma, e somente uma instância de uma classe. Essa instância deve ser global.
Em Hogwarts só existe uma quadra de Quadribol: _QPitch.py_. Como vamos garantir que só existirá uma instância da classe _QPitch.py_ no código pra que só dois times possam jogar de cada vez?

## Solução

Singleton:
* Provê ponteiro global para o objeto na primeira vez que ele for instanciado.
* A solução encontrada para a instanciação única da quadra de quadribol de Hogwarts foi criar uma metaclasse "Singleton" com uma variável do tipo dicionário que guarda suas instancias ("_instancias"), se a quadra ja foi criada ela está nessa lista e não vai ser criada de novo, se não ela é criada pela primeira vez.
* O uso de metaclasses provê o reuso, por exemplo: se quisermos ter somente uma instanciação do "Mapa do Maroto" basta criar uma classe para este e defininir "Singleton" como sua metaclasse, como é feito no código da classe da quadra de quadribol (Qpitch).


![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Singleton_example.png "Singleton")
