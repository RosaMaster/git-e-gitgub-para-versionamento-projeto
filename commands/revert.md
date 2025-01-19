### Comando git revert

O comando git revert é usado para desfazer mudanças introduzidas por commits anteriores, criando um novo commit que reverte as mudanças. Ao contrário do git reset, que altera o histórico de commits, o git revert preserva o histórico, tornando-o uma opção mais segura para desfazer mudanças em projetos colaborativos

#### Usos Comuns do git revert

1. Reverter um commit específico
    `Este comando cria um novo commit que desfaz as mudanças introduzidas pelo commit especificado`

~~~bash
git revert <commit-hash>
~~~

2. Reverter uma série de commits
    `Este comando cria novos commits que desfazem as mudanças introduzidas por uma série de commits`

~~~bash
git revert <commit-hash-inicial>..<commit-hash-final>
~~~


Veja um exemplo de fluxo de trabalho com Revert [AQUI](./fluxo-de-trabalho-com-revert.md)

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#comando-git-revert)
