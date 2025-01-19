### Comando git reset

O comando git reset é uma ferramenta poderosa no Git usada para desfazer mudanças. Ele pode ser usado para redefinir o índice (staging area), o diretório de trabalho ou ambos para um estado anterior. O git reset pode ser perigoso se não for usado corretamente, pois pode alterar o histórico de commits.

#### Modos de git reset

1. Soft Reset (--soft)
    - Mantém as mudanças no índice e no diretório de trabalho
    - Apenas move o ponteiro da branch atual para o commit especificado
    - Útil para desfazer commits sem perder as mudanças

~~~bash
git reset --soft <commit-hash>
~~~

2. Mixed Reset (--mixed)
    - Redefine o índice, mas mantém as mudanças no diretório de trabalho
    - Este é o modo padrão se nenhum argumento for fornecido
    - Útil para desfazer commits e preparar as mudanças para um novo commit

~~~bash
git reset --mixed <commit-hash>
~~~

3. Hard Reset (--hard)
    - Redefine o índice e o diretório de trabalho para o estado do commit especificado
    - Todas as mudanças não comitadas serão perdidas
    - Útil para desfazer commits e descartar todas as mudanças

~~~bash
git reset --hard <commit-hash>
~~~

Veja um exemplo de fluxo de trabalho com Reset [AQUI](./fluxo-de-trabalho-com-reset.md)

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#comando-git-reset)
