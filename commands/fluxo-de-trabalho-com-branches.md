### Fluxo de Trabalho com Branches

1. Criar uma nova **branch**: Crie uma nova branch a partir da branch principal para trabalhar em uma nova funcionalidade ou correção de bug

~~~bash
git checkout -b nova-feature
~~~

2. Desenvolver e comitar: Faça as alterações necessárias e comite-as na nova branch

~~~bash
git add .
git commit -m "Adicionar nova funcionalidade"
~~~

3. Push para o repositório remoto: Envie a branch para o repositório remoto

~~~bash
git push origin nova-feature
~~~

4. Abrir um Pull Request: No repositório remoto (por exemplo, GitHub), abra um Pull Request para mesclar a nova branch na branch principal

5. Revisão e merge: Após a revisão e aprovação, mescle a branch na branch principal

~~~bash
git checkout main
git merge nova-feature
~~~

6. Deletar a branch: Opcionalmente, delete a branch de feature após o merge para manter o repositório limpo

~~~bash
git branch -d nova-feature
~~~

[**[ VOLTAR ]**](./checkout.md) <===> [**[ INICIO ]**](#fluxo-de-trabalho-com-branches)
