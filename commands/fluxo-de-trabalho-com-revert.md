### Fluxo de Trabalho com git revert

1. Identifique o commit a ser revertido: Use git log para encontrar o hash do commit que você deseja reverter

~~~bash
git log
~~~

2. Execute o revert: Use o comando git revert para criar um novo commit que desfaz as mudanças do commit especificado

~~~bash
git revert <commit-hash>
~~~

3. Resolva conflitos (se houver): Se ocorrerem conflitos, resolva-os manualmente e finalize o revert

~~~bash
git add .
git revert --continue
~~~

4. Finalize o processo: Após resolver os conflitos e finalizar o revert, o novo commit será aplicado à branch atual

~~~bash
git status
~~~

#### Comparação com git reset

- **git revert**: Cria um novo commit que desfaz as mudanças de um commit anterior, preservando o histórico de commits. Ideal para projetos colaborativos
- **git reset**: Altera o histórico de commits, movendo o ponteiro da branch atual para um commit anterior. Pode resultar na perda de mudanças não comitadas e deve ser usado com cautela

`O comando git revert é uma ferramenta essencial para desfazer mudanças de forma segura e colaborativa no Git, preservando o histórico de commits e facilitando a manutenção do código`

Veja um exemplo prático de trabalho com Reset [AQUI](./exemplo-revert-pratico.md)

[**[ VOLTAR ]**](./revert.md) <===> [**[ INICIO ]**](#fluxo-de-trabalho-com-git-revert)
