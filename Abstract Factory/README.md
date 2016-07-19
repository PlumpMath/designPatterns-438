## Problema

Se uma app deseja ser portável, ele precisa encapsular dependências de plataformas.
Nesse caso queremos que "AtualizaçãoAnual" seja uma interface global no mundo dos bruxos e as plataformas que são anualmente atualizadas são as escolas e o ministério.

## Solução

Abstract Factory provê:
* Interface para criar famílias (ou objetos dependentes) sem especificar suas classes concretas (EscolaDeMagia, MinistérioDeMagia)
* Hierarquia que encapsula muitas possíveis plataformas (AtualizaçãoAnual de diversos países com suas respectivas escolas e ministério)

![alt text](https://github.com/Vinicoreia/designPatterns/blob/master/etc/Abstract_Factory_example.png "Abstract Factory")
