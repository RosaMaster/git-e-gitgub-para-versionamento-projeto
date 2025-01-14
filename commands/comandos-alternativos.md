### Comando alternativos git > 2.32v

Com a introdução do **Git > 2.23v**, novos comandos foram adicionados para substituir algumas funcionalidades do git checkout

1. **git switch** é usado especificamente para mudar de branch<br><br>

~~~bash
git switch nome-da-branch
git switch -c nome-da-nova-branch
~~~

2. **git restore**: Usado para restaurar arquivos<br><br>

~~~bash
git restore caminho/do/arquivo
git restore --source nome-da-branch caminho/do/arquivo
~~~

Esses novos comandos ajudam a tornar o uso do Git mais intuitivo e específico para cada tarefa.

O comando git checkout é uma ferramenta essencial no Git, permitindo uma navegação eficiente entre branches, restauração de arquivos e criação de novas branches, facilitando o fluxo de trabalho no desenvolvimento de software.

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#comando-alternativos-git--232v)
