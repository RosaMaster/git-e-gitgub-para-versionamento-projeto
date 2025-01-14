### Exemplos Práticos

Aplicar um commit específico

`Este comando aplica o commit com a hash a1b2c3d4 à branch atual`

~~~bash
git cherry-pick a1b2c3d4
~~~

Aplicar uma série de commits

`Este comando aplica todos os commits desde a1b2c3d4 até d4e5f6g7 à branch atual`

~~~bash
git cherry-pick a1b2c3d4^..d4e5f6g7
~~~

Aplicar múltiplos commits específicos

`Este comando aplica os commits a1b2c3d4, e5f6g7h8 e i9j0k1l2 à branch atual`

~~~bash
git cherry-pick a1b2c3d4 e5f6g7h8 i9j0k1l2
~~~

#### Considerações Importantes

**Conflitos**: Assim como em uma mesclagem (merge), o git cherry-pick pode resultar em conflitos se as mudanças nos commits selecionados entrarem em conflito com o código na branch atual. Você precisará resolver esses conflitos manualmente.

**Histórico de Commits**: O git cherry-pick cria novos commits na branch de destino que são cópias dos commits originais. Isso significa que os commits terão novos hashes, mas manterão as mesmas mensagens de commit e mudanças de código.

**Uso Responsável**: Use git cherry-pick com cuidado, especialmente em projetos colaborativos, pois ele pode complicar o histórico de commits se usado excessivamente.

<br>

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#exemplos-práticos)

