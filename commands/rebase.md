### Comando git rebase

O comando git rebase é usado para aplicar commits de uma branch em outra, criando um histórico de commits mais linear e limpo. Ele é uma alternativa ao git merge, mas ao invés de criar um commit de mesclagem, ele reaplica os commits da branch de origem na branch de destino

#### Usos Comuns do git rebase

1. Rebase de uma branch em outra

    `Este comando move os commits da feature-branch para o topo dos commits da main, criando um histórico linear`

~~~bash
git checkout feature-branch
git rebase main
~~~

2. Interativo (Interactive Rebase)

    `Este comando permite editar, reordenar, combinar ou descartar commits em uma série de n commits a partir do HEAD`

Veja um exemplo de fluxo de trabalho com Rebase [AQUI](./fluxo-de-trabalho-com-rebase.md)

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#comando-git-rebase)
