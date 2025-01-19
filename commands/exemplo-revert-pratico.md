### Exemplos Revert Práticos

Reverter um commit específico

`Este comando cria um novo commit que desfaz as mudanças introduzidas pelo commit com a hash a1b2c3d4`

~~~bash
git revert a1b2c3d4
~~~

Reverter uma série de commits

`Este comando cria novos commits que desfazem as mudanças introduzidas pelos commits desde a1b2c3d4 até d4e5f6g7`

~~~bash
git revert a1b2c3d4..d4e5f6g7
~~~

#### Considerações Importantes

- **Preservação do Histórico**: O git revert preserva o histórico de commits, tornando-o uma opção segura para desfazer mudanças em branches compartilhadas
- **Conflitos**: Assim como em uma mesclagem (merge), o git revert pode resultar em conflitos se as mudanças a serem revertidas entrarem em conflito com o código atual. Você precisará resolver esses conflitos manualmente
- **Mensagens de Commit**: O git revert cria novos commits com mensagens padrão que indicam quais commits foram revertidos. Você pode editar essas mensagens conforme necessário

[**[ VOLTAR ]**](./fluxo-de-trabalho-com-revert.md) <===> [**[ INICIO ]**](#exemplos-reset-práticos)
