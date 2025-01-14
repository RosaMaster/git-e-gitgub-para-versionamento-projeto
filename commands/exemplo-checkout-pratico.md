### Exemplos Práticos

Mudar para a branch **main**

~~~bash
git checkout main
~~~

Criar uma nova branch chamada **feature-x** e mudar para ela

~~~bash
git checkout -b feature-x
~~~

Restaurar um arquivo chamado **index.html** da branch **main**

~~~bash
git checkout main -- index.html
~~~

Mudar para um commit específico usando seu **hash**

~~~bash
git checkout 1a2b3c4d
~~~

<br>

#### Considerações Importantes

**Mudança de Branch**: Quando você muda de uma branch para outra, o Git atualiza os arquivos no seu diretório de trabalho para refletir o estado da nova branch. Certifique-se de que todas as suas mudanças estejam comitadas ou armazenadas (stashed) antes de mudar de branch para evitar perda de trabalho.

**Criação de Branches**: Usar git checkout -b nome-da-nova-branch é uma maneira rápida de criar e mudar para uma nova branch em um único comando.

**Restaurar Arquivos**: O comando git checkout pode ser usado para restaurar arquivos específicos para o estado de outra branch ou commit, o que é útil para desfazer mudanças indesejadas.

<br>

`Alternativas ao git checkout:` [**SWITCH**](./comandos-alternativos.md)

<br>

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#exemplos-práticos)

