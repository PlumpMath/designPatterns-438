## Problema

Suponha que os alunos sempre precisam contruir a grade-horária com no mínimo 3 temas diferntes:
* Magia (exemplo: Defesa contra as Artes das Trevas e Transfiguração)
* Educação Física (exemplo: Vôo e Duelo)
* História (exemplo: História da Magia e Runas Antigas)

O problema é otimizar a implementação.

## Solução

Criamos interfaces (Magia.py, EducFisica.py e Historia.py) para as matérias do mesmo tipo.
Apenas na contrução da grade é que decidimos quais matérias pegar.

#### Disciplina.py 
#### ^
#### Magia.py| EducFisica.py | Historia.py
#### Trevas	| Jogo	| Leitura
#### Mutação	| Luta	| Campo
#### Feitiço	|

Exemplos de grade:
* Grade1(Trevas, Luta, Campo)
* Grade2(Feitiço, Luta, Leitura)


![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Abstract_Factory_example.png "Abstract Factory")
