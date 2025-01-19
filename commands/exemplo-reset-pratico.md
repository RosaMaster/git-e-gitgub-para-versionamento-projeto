### Exemplos Reset Práticos

Soft Reset para o commit anterior

`Este comando move o ponteiro da branch atual para o commit anterior, mantendo as mudanças no índice e no diretório de trabalho`

~~~bash
git reset --soft HEAD~1
~~~

Mixed Reset para um commit específico

`Este comando redefine o índice para o estado do commit especificado, mantendo as mudanças no diretório de trabalho`

~~~bash
git reset <commit-hash>
~~~

Hard Reset para o commit anterior

`Este comando redefine o índice e o diretório de trabalho para o estado do commit anterior, descartando todas as mudanças não comitadas`

~~~bash
git reset --hard HEAD~1
~~~

#### Considerações Importantes

    - Perda de Dados: O git reset --hard pode resultar na perda de mudanças não comitadas. Use-o com cautela
    - Histórico de Commits: O git reset altera o histórico de commits da branch atual. Evite usá-lo em branches compartilhadas com outros desenvolvedores.
    - Alternativas: Para desfazer mudanças de forma mais segura, considere usar git revert ou git restore

[**[ VOLTAR ]**](./fluxo-de-trabalho-com-reset.md) <===> [**[ INICIO ]**](#exemplos-reset-práticos)
