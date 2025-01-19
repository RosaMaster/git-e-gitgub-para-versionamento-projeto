### Comandos git fetch, git pull e git push

Os comandos git **fetch**, git **pull** e git **push** são usados para sincronizar o repositório local com o repositório remoto. Cada um desses comandos tem uma função específica no fluxo de trabalho do Git

#### git fetch

O comando git fetch é usado para baixar commits, arquivos e referências de um repositório remoto para o repositório local. Ele atualiza as referências locais, mas não mescla as mudanças no diretório de trabalho

1. Uso básico

`Este comando baixa todas as mudanças do repositório remoto chamado origin`

~~~bash
git fetch origin
~~~

2. Uso específico

`Este comando baixa as mudanças de uma branch específica do repositório remoto`

~~~bash
git fetch origin nome-da-branch
~~~

#### git pull

O comando git pull é usado para baixar e mesclar mudanças do repositório remoto para o repositório local. Ele é uma combinação de git fetch e git merge

1. Uso básico

`Este comando baixa as mudanças da branch especificada do repositório remoto e as mescla na branch atual`

~~~bash
git pull origin nome-da-branch
~~~

2. Uso com rebase

`Este comando baixa as mudanças e as aplica no topo da branch atual, mantendo um histórico de commits mais linear`

~~~bash
git pull --rebase origin nome-da-branch
~~~

#### git push

O comando git push é usado para enviar commits do repositório local para o repositório remoto. Ele atualiza o repositório remoto com as mudanças feitas localmente

1. Uso básico

`Este comando envia os commits da branch local especificada para a branch correspondente no repositório remoto`

~~~bash
git push origin nome-da-branch
~~~

2. Uso com rebase

`Este comando força a atualização do repositório remoto, sobrescrevendo qualquer histórico de commits conflitante`

~~~bash
git push --force origin nome-da-branch
~~~

#### Considerações Importantes

- **git fetch**: Útil para verificar as mudanças no repositório remoto sem afetar o diretório de trabalho local. Ideal para revisar o que mudou antes de mesclar
- **git pull**: Combina fetch e merge, atualizando o diretório de trabalho local com as mudanças do repositório remoto. Pode resultar em conflitos que precisam ser resolvidos manualmente
- **git push**: Envia mudanças locais para o repositório remoto. Certifique-se de que sua branch local está atualizada com a branch remota para evitar conflitos

`Esses comandos são essenciais para manter a sincronização entre o repositório local e o repositório remoto, facilitando a colaboração e o gerenciamento de versões no desenvolvimento de software`

[**[ VOLTAR ]**](./comandos-git.md) <===> [**[ INICIO ]**](#comandos-git-fetch-git-pull-e-git-push)

[**[ FETCH ]**](#git-fetch) <===> [**[ PULL ]**](#git-pull) <===> [**[ PUSH ]**](#git-push)
