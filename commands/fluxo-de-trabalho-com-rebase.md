### Fluxo de Trabalho com git rebase

1. Mudar para a branch que será rebased

~~~bash
git checkout feature-branch
~~~

2. Executar o rebase

~~~bash
git rebase main
~~~

3. Resolver conflitos (se houver):
    - Resolva os conflitos manualmente.
    - Adicione os arquivos resolvidos ao índice:

~~~bash
git add .
~~~

- Continue o rebase:

~~~bash
git rebase --continue
~~~

4. Abortar o rebase (se necessário)

~~~bash
git rebase --abort
~~~

#### Rebase Interativo

O rebase interativo (-i) permite editar, reordenar, combinar ou descartar commits. É útil para limpar o histórico de commits antes de mesclar uma branch

1. Iniciar um rebase interativo

`Este comando abre um editor de texto onde você pode editar os últimos 3 commits`

~~~bash
git rebase -i HEAD~3
~~~

##### Opções no rebase interativo

- **pick**: Manter o commit

- **reword**: Editar a mensagem do commit

- **edit**: Editar o commit

- **squash**: Combinar o commit com o anterior

- **fixup**: Combinar o commit com o anterior, descartando a mensagem do commit

- **drop**: Descartar o commit

`O comando git rebase é uma ferramenta poderosa para manter um histórico de commits limpo e linear. Compreender como e quando usá-lo é crucial para um fluxo de trabalho eficiente e colaborativo no Git`

Veja um exemplo prático de trabalho com Reset [AQUI](./exemplo-rebase-pratico.md)

[**[ VOLTAR ]**](./rebase.md) <===> [**[ INICIO ]**](#fluxo-de-trabalho-com-git-rebase)
