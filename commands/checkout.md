### Comando git checkout

O comando **git checkout** é usado para navegar entre branches, restaurar arquivos e criar novas branches no Git. 

Ele é uma ferramenta versátil que desempenha várias funções importantes no fluxo de trabalho do Git.

#### Usos Comuns do git checkout

1. Mudar para uma branch existente<br><br>

`Este comando muda o diretório de trabalho para a branch especificada, atualizando os arquivos no diretório de trabalho para corresponder ao estado da branch`

~~~bash
git checkout nome-da-branch
~~~

2. Criar e mudar para uma nova branch<br><br>

`Este comando cria uma nova branch a partir da branch atual e muda para ela`

~~~bash
git checkout -b nome-da-nova-branch
~~~

3. Restaurar um arquivo específico

`Este comando restaura o arquivo especificado para o estado da branch indicada`

~~~bash
git checkout nome-da-branch -- caminho/do/arquivo
~~~

4. Restaurar todos os arquivos para um commit específico

`Este comando atualiza o diretório de trabalho para o estado de um commit específico, usando o hash do commit`

~~~bash
git checkout <commit-hash>
~~~

Veja um exemplo prático de checkout [AQUI](./exemplo-checkout-pratico.md)

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#comando-git-checkout)
