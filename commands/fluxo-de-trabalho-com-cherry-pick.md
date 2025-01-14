### Fluxo de Trabalho com git cherry-pick

1. Identifique o commit a ser cherry-picked: Use git log para encontrar o hash do commit que você deseja aplicar

~~~bash
git log
~~~

2. Mude para a branch de destino: Certifique-se de estar na branch onde você deseja aplicar o commit

~~~bash
git checkout nome-da-branch
~~~

3. Execute o cherry-pick: Aplique o commit específico à branch atual

~~~bash
git cherry-pick <commit-hash>
~~~

4. Resolva conflitos (se houver): Se ocorrerem conflitos, resolva-os manualmente e finalize o cherry-pick

~~~bash
git add .
git cherry-pick --continue
~~~

5. Finalize o processo: Após resolver os conflitos e finalizar o cherry-pick, o commit será aplicado à branch atual

`O comando git cherry-pick é uma ferramenta poderosa para aplicar commits específicos de uma branch para outra, permitindo maior flexibilidade e controle no gerenciamento de mudanças no código`

[**[ VOLTAR ]**](./checkout.md) <===> [**[ INICIO ]**](#fluxo-de-trabalho-com-branches)
