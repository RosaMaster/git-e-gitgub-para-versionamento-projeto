### Fluxo de Trabalho com git reset

1. Identifique o commit para redefinir: Use git log para encontrar o hash do commit para o qual você deseja redefinir

~~~bash
git log
~~~

2. Escolha o modo de reset: Decida se você precisa de um reset **--soft**, **--mixed** ou **--hard**

3. Execute o reset: Use o comando apropriado para redefinir o índice e/ou o diretório de trabalho

~~~bash
git reset --soft <commit-hash>
git reset --mixed <commit-hash>
git reset --hard <commit-hash>
~~~

4. Verifique o estado: Use git status para verificar o estado do repositório após o reset

~~~bash
git status
~~~

`O comando git reset é uma ferramenta versátil e poderosa para desfazer mudanças no Git. Compreender os diferentes modos de reset e suas implicações é crucial para usá-lo de forma eficaz e segura`

Veja um exemplo prático de trabalho com Reset [AQUI](./exemplo-reset-pratico.md)

[**[ VOLTAR ]**](./reset.md) <===> [**[ INICIO ]**](#fluxo-de-trabalho-com-git-reset)
