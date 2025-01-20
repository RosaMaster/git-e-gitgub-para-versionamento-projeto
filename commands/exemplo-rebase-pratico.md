### Exemplos Rebase Práticos

Rebase de uma branch em outra

`Este comando reaplica os commits da feature-branch no topo da main`

~~~bash
git checkout feature-branch
git rebase main
~~~

Rebase interativo para editar commits

`Este comando abre um editor de texto onde você pode editar os últimos 3 commits`

~~~bash
git rebase -i HEAD~3
~~~

Hard Reset para o commit anterior

`Este comando redefine o índice e o diretório de trabalho para o estado do commit anterior, descartando todas as mudanças não comitadas`

~~~bash
git reset --hard HEAD~1
~~~

#### Considerações Importantes

- **Histórico Linear**: O git rebase cria um histórico de commits mais linear e limpo, o que pode fa**cilitar a leitura e a revisão do histórico

- **Conflitos**: Assim como no git merge, o git rebase pode resultar em conflitos que precisam ser re**solvidos manualmente

- **Reescrita de Histórico**: O git rebase reescreve o histórico de commits, criando novos hashes para os commits reaplicados. Isso pode causar problemas em branches compartilhadas com outros desenvolvedores

- **Uso Responsável**: Evite usar git rebase em branches que já foram compartilhadas com outros desenvolvedores, pois isso pode complicar a sincronização do repositório

[**[ VOLTAR ]**](./fluxo-de-trabalho-com-reset.md) <===> [**[ INICIO ]**](#exemplos-reset-práticos)
